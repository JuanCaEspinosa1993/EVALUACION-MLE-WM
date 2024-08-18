from src.data_ingestion import load_data, read_csv_files
from src.data_processing import *
from src.model_training import create_model
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

    features_dict = x_features(data_dict_city)
    y_dict = y_features(data_dict_city)

    ## Guardando features Dataframes en .csv
    for city, df_city in features_dict.items():
        filename = f'{city}.csv'
        df_city.to_csv(f"data/interim/{filename}", index=False)

    ## Guardando f_dict Dataframes en .csv
    for city, df_city in y_dict.items():
        filename = f'val+{city}.csv'
        df_city.to_csv(f"data/interim/{filename}", index=False)

    ##Entrenando modelo
    features_path = 'data/interim/Canberra.csv'
    labels_path = 'data/interim/val+Canberra.csv'
    model_path_to_save = 'models'
    model = create_model(features_path, labels_path, model_path_to_save)


    

if __name__ == '__main__':
    main()