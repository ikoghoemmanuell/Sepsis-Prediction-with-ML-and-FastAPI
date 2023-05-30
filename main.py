from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

# Load the model and and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Define the input data model
class InputData(BaseModel):
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    Patient_age: int

# Convert the input values to a pandas DataFrame with the appropriate column names
def input_df_creator(data: InputData):
    input_data = pd.DataFrame(data.dict(), index=[0])
    return input_data

# Define the churn prediction endpoint
@app.post("/predict_churn")
def predict_churn(data: InputData):
    input_df = input_df_creator(data)

    # Scale numerical variables
    num_cols = input_df.select_dtypes(include=['int64', 'float64']).columns
    num_scaled = scaler.transform(input_df)
    
    # processed_df = num_scaled
    processed_df = pd.DataFrame(num_scaled, columns = ['Blood_Work_R1', 'Blood_Pressure', 'Blood_Work_R3', 'BMI', 'Blood_Work_R4', 'Patient_age'])

    # Make prediction
    prediction = model.predict(processed_df)
    sepsis_prediction = bool(prediction[0])

    return {"prediction": sepsis_prediction}
