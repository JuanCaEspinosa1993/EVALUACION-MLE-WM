from src.data_ingestion import load_data, read_csv_files
import os

def main():
    #Cargar los datos
    df = load_data("data/raw/weatherAUs.csv")
    print(df.head())

if __name__ == '__main__':
    main()