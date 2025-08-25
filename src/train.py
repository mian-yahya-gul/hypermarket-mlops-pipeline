import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import sys


def train_model(data_path: str, model_path: str):
    # Load processed data
    df = pd.read_csv(data_path, sep="\t")

    # Features and target
    X = df[["Day"]]
    y = df["Sales"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save model
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model trained and saved to {model_path}")


if __name__ == "__main__":
    input_path = sys.argv[1]   # e.g. data/processed_sales.csv
    output_path = sys.argv[2]  # e.g. model.pkl
    train_model(input_path, output_path)
