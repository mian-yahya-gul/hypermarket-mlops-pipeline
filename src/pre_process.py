import pandas as pd
import sys

def preprocess_sales(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df = df.fillna(0)  # simple cleaning
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    preprocess_sales(input_path, output_path)
