from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import logging
import uvicorn
import os

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API
app = FastAPI(title="API")

# Util Functions & Classes

# Load the model and scaler
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def load_scaler():
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return scaler

model = load_model()
scaler = load_scaler()

def predict(df, endpoint="simple"):
    """Take a dataframe as input and use it to make predictions"""
    print(f"[INFO] 'predict' function has been called through the endpoint: {endpoint}")
    print(f"[INFO] Input dataframe:\n{df}")

    # Scaling
    scaled_df = scaler.transform(df)
    print(f"INFO: Scaled dataframe:\n{scaled_df}")

    # Prediction
    prediction = model.predict_proba(scaled_df)
    print(f"INFO: Prediction probabilities:\n{prediction}")

    # Formatting of the prediction
    highest_proba = prediction.max(axis=1)
    print(f"INFO: Highest probabilities: {highest_proba}")

    highest_proba_idx = prediction.argmax(axis=1)
    print(f"INFO: Highest probability indexes: {highest_proba_idx}")

    predicted_classes = [labels[i] for i in highest_proba_idx]
    print(f"INFO: Predicted classes: {predicted_classes}")

    df["predicted_proba"] = highest_proba
    df["predicted_label"] = predicted_classes
    print(f"INFO: DataFrame with prediction:\n{df}")

    parsed = df.to_dict('records')
    return parsed


class Patient(BaseModel):
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    Patient_age: int


class Patients(BaseModel):
    all: list[Patient]
    
    @classmethod
    def return_list_of_dict(cls):
        return [i.dict() for i in cls.all]


labels = load_model().classes_

# Endpoints
@app.get("/")
def root():
    return {"API": "This is an API for sepsis prediction."}

@app.get("/checkup")
def checkup(a: int = None, b: int = 0):
    return {"a": a, "b": b}

## ML endpoint
@app.post("/predict")
def predict_sepsis(patient: Patient):
    """Make prediction with the passed data"""
    data = pd.DataFrame(patient.dict(), index=[0])
    parsed = predict(df=data)
    return {"output": parsed}

@app.post("/predict_multi")
def predict_sepsis_for_multiple_patients(patients: Patients):
    """Make prediction with the passed data"""
    data = pd.DataFrame(patients.return_list_of_dict())
    parsed = predict(df=data, endpoint="multi")
    return {"output": parsed}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
