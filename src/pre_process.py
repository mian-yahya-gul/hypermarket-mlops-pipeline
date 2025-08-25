import pandas as pd
import sys

def preprocess_sales(input_path: str, output_path: str):
    # Explicitly tell pandas that input file may be tab/space separated
    df = pd.read_csv(input_path, sep=r"\s+")
    
    df = df.fillna(0)
    
    # Force output with commas
    df.to_csv(output_path, index=False, sep=",")


if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    preprocess_sales(input_path, output_path)
