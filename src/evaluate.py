import sys
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

def evaluate_model(model_path: str, data_path: str, metrics_path: str):
    # Load model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Load test data
    df = pd.read_csv(data_path)
    X = df[["Day"]]
    y = df["Sales"]

    # Predict
    y_pred = model.predict(X)

    # Calculate metrics
    mse = mean_squared_error(y, y_pred)

    # Save metrics
    with open(metrics_path, "w") as f:
        f.write(f"mse: {mse}\n")

    print(f"Evaluation complete. MSE: {mse}")

if __name__ == "__main__":
    model_path = sys.argv[1]     # model.pkl
    data_path = sys.argv[2]      # data/processed_sales.csv
    metrics_path = sys.argv[3]   # metrics.json or txt
    evaluate_model(model_path, data_path, metrics_path)
