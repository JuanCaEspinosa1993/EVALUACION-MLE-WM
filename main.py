from src.data_ingestion import load_data, read_csv_files
from src.data_processing import *
import os

def main():
    #Cargar los datos
    df = load_data("data/raw/weatherAUs.csv")
    
    # Procesamiento de datos
    data = categorize_feature(df)
    percent_of_null_values = df_null_values_percent(data)
    data_dict_city = df_dict_city(data)
    data_dict_city = delete_null_columns(data_dict_city)
    data_dict_city = fill_column_with_mode(data_dict_city)
    data_dict_city = fill_column_with_mean(data_dict_city)
    features = build_features(data_dict_city)
    print(features)


if __name__ == '__main__':
    main()