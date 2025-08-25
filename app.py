from fastapi import FastAPI
from src.predict import predict_sales

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hypermarket Sales Prediction API"}


