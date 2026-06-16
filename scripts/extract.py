# Extract data from CSV files

import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    print("Extract module ready")
