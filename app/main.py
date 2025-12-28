from fastapi import FastAPI
import joblib
import pandas as pd
from utils import preprocess

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def root():
    return {"message": "AI Ops Service Running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    X = preprocess(df)
    pred = model.predict(X)
    return {"prediction": pred.tolist()}

