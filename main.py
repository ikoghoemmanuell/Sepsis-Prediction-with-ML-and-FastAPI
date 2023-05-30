from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import logging
import uvicorn

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load the model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Define the input data model using Pydantic
class InputData(BaseModel):
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    Patient_age: int

# Convert the input values to a pandas DataFrame with appropriate column names
def input_df_creator(data: InputData):
    input_data = pd.DataFrame(data.dict(), index=[0])
    return input_data

# Define the sepsis prediction endpoint
@app.post("/predict_sepsis")
def predict_sepsis(data: InputData):
    input_df = input_df_creator(data)

    # Scale numerical variables
    num_cols = input_df.select_dtypes(include=['int64', 'float64']).columns
    num_scaled = scaler.transform(input_df)

    processed_df = pd.DataFrame(num_scaled, columns=num_cols)

    # Make prediction
    prediction = model.predict(processed_df)
    sepsis_prediction = bool(prediction[0])

    return {"prediction": sepsis_prediction}

# Root endpoint
@app.get("/")
def root():
    return {"API": "This is an API for sepsis prediction."}

# Checkup endpoint
@app.get("/checkup")
def checkup(a: int = None, b: int = 0):
    return {"a": a, "b": b}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
