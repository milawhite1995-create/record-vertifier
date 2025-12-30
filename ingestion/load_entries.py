import pandas as pd

def load_entries(path):
    return pd.read_csv(path).to_dict(orient="records")