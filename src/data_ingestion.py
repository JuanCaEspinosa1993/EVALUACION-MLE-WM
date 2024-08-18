import os
import pandas as pd

def read_csv_files(input_dir):
    datasets = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_dir, file_name)
            df = pd.read_csv(file_path)
            datasets.append(df)
    return datasets

def load_data(filepath):
    return pd.read_csv(filepath)
