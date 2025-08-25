import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model(data_path: str, model_path: str):
    df = pd.read_csv(data_path)
    X = df[["Day"]]
    y = df["Sales"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
