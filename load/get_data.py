# Import necessary libraries
import pandas as pd

def load_data_from_csv(file_path: str):
    raw_s = r'{}'.format(file_path)
    return pd.read_csv(raw_s)