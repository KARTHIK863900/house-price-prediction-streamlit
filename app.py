from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

model = pickle.load(open("lreg.pkl", "rb"))

class InputData(BaseModel):
    Area: float
    Room: int
    Parking: int
    Warehouse: int
    Elevator: int

@app.get("/")
def home():
    return {"message": "House Price Prediction API"}

@app.post("/predict")
def predict(data: InputData):

    df = pd.DataFrame({
        "Area":[data.Area],
        "Room":[data.Room],
        "Parking":[data.Parking],
        "Warehouse":[data.Warehouse],
        "Elevator":[data.Elevator]
    })

    prediction = model.predict(df)

    return {
        "Predicted Price": float(prediction[0])
    }
