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

    # Prediction
    prediction = model.predict_proba(scaled_df)
    print(f"INFO: Prediction probabilities:\n{prediction}")

    # Formatting of the prediction
    highest_proba = prediction.max(axis=1)

    highest_proba_idx = prediction.argmax(axis=1)

    predicted_labels = ["Negative" if i == 0 else "Positive" for i in highest_proba_idx]
    print(f"INFO: Predicted labels: {predicted_labels}")

    response = []
    for label, proba in zip(predicted_labels, highest_proba):
        output = {
            "predicted_proba": proba,
            "predicted_label": label
        }
        response.append(output)

    return response


class Patient(BaseModel):
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    Patient_age: int

class Patients(BaseModel):
    all_patients: list[Patient]

    @classmethod
    def return_list_of_dict(cls, patients: "Patients"):
        patient_list = []
        for patient in patients.all_patients:
            patient_dict = patient.dict()
            patient_list.append(patient_dict)
        return patient_list


labels = load_model().classes_

# Endpoints
@app.get("/")
def root():
    return {"API": "This is an API for sepsis prediction."}

@app.get("/checkup")
def checkup(a: int = None, b: int = 0):
    return {"a": a, "b": b}

## Prediction endpoint
@app.post("/predict")
def predict_sepsis_for_multiple_patients(patients: Patients):
    """Make prediction with the passed data"""
    data = pd.DataFrame(Patients.return_list_of_dict(patients))
    parsed = predict(df=data, endpoint="multi")
    return {"output": parsed}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
