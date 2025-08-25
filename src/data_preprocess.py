import pandas as pd

def preprocess_sales(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df = df.fillna(0)
    df.to_csv(output_path, index=False)
