import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

current_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
csv_path = os.path.join(parent_dir, 'data', 'raw', 'weatherAUs.csv')
data = pd.read_csv(csv_path)
Loc = data['Location'].unique()

def categorize_feature(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    ## Categorizacion de variables.
    data['RainToday'] = (data['RainToday'] == 'Yes')*1
    data['RainTomorrow'] = (data['RainTomorrow'] == 'Yes')*1

    Ab_WD = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S', 'SSW','SW','WSW','W','WNW','NW','NNW']
    WD = [0,22.5,45,67.5,90,112.5,135,157.5,180,202.5,225,247.5,270,292.5,315,337.5]
    Col_WindDir = ['WindGustDir','WindDir9am','WindDir3pm']

    #Dataframe de mapeo
    Wind_Dir = pd.DataFrame({
        'Ab_WD': Ab_WD,
        'WD': WD
        })
    #convertir a diccionario
    wind_dir_map = dict(zip(Wind_Dir['Ab_WD'], Wind_Dir['WD']))
    for column in Col_WindDir:
        data[column] = data[column].map(wind_dir_map)

    return data


def corr_data(data: pd.DataFrame) -> pd.DataFrame:
    data.select_dtypes(include=[float, int]).corr()
    return data


def heatmap_data(data: pd.DataFrame) -> None:
    plt.figure(figsize=(20,12))
    sns.heatmap(corr_data(data),annot=True)


def df_null_values_percent(data: pd.DataFrame)-> pd.Series:
    null_values_percent = (data.isnull().sum()*100)/len(data.index)
    return null_values_percent


def df_dict_city(data: pd.DataFrame) -> dict:
    df_dict_Loc = {city: data[data['Location'] == city] for city in Loc}
    return df_dict_Loc


def df_null_values_percent_by_city(df_dict_Loc: dict) -> dict:
    null_val_perc = {}
    for city, df_city in df_dict_Loc.items():
        null_val_perc[city] = (df_city.isnull().sum()*100) / len(df_city)
    return null_val_perc


def delete_null_columns(df_dict_Loc: dict) -> dict:
    null_val_perc = df_null_values_percent_by_city(df_dict_Loc)
    for city in list(df_dict_Loc.keys()):
        cols_to_drop = null_val_perc[city][null_val_perc[city] == 100.0].index
        df_dict_Loc[city].drop(columns=cols_to_drop, axis=1, inplace=True)
        null_val_perc[city].drop(labels=cols_to_drop, inplace=True)
    return df_dict_Loc


def fill_column_with_mode(df_dict_Loc: dict) -> dict:
    Col_Mode =['WindGustDir','WindDir9am','WindDir3pm','Cloud9am','Cloud3pm']

    for city, df_city in df_dict_Loc.items():
        for column in Col_Mode:
            if column in df_city.columns:
                mode_value = df_city[column].mode()[0]
                df_city[column].fillna(mode_value, inplace=True)
    return df_dict_Loc

def fill_column_with_mean(df_dict_Loc: dict) -> dict:
    for city, df_city in df_dict_Loc.items():
        numeric_cols = df_city.select_dtypes(include='number').columns
        numeric_cols = [column for column in numeric_cols if column in df_city.columns]
        df_city[numeric_cols] = df_city[numeric_cols].fillna(df_city[numeric_cols].mean())
    return df_dict_Loc


def coef_corr_by_city(df_dict_Loc: dict) -> dict:
    coef_corr = {}
    for city, df_city in df_dict_Loc.items():
        coef_corr[city]= df_dict_Loc[city].select_dtypes(include=[float, int]).corr()
    return coef_corr


def coef_corr_positive_by_city(df_dict_Loc: dict)  -> dict:
    coef_corr = coef_corr_by_city(df_dict_Loc)
    coef_corr_p = {}
    for key in df_dict_Loc.keys():
        coef_corr_p[key]= coef_corr[key][coef_corr[key]['RainTomorrow']>= .1]
        coef_corr_p[key]=coef_corr_p[key].drop(['RainTomorrow'],axis=0)
    return coef_corr_p


def coef_corr_negative_by_city(df_dict_Loc: dict) -> dict:
    coef_corr = coef_corr_by_city(df_dict_Loc)
    coef_corr_n = {}
    for key in df_dict_Loc.keys():
        coef_corr_n[key]= coef_corr[key][coef_corr[key]['RainTomorrow']<= -.1]
    return coef_corr_n

def concat_feature_by_coef_corr(df_dict_Loc: dict) -> dict:
    total_len = {elem : list() for elem in Loc}
    coef_corr_positive = coef_corr_positive_by_city(df_dict_Loc)
    coef_corr_negative = coef_corr_negative_by_city(df_dict_Loc)
    for key in df_dict_Loc.keys():
        total_len[key].append(len(coef_corr_positive[key].index) +len(coef_corr_negative[key].index))
    return total_len

def build_features(df_dict_Loc: dict) -> dict:
    features = {elem : list() for elem in Loc}
    features_concat = concat_feature_by_coef_corr(df_dict_Loc)
    coef_corr_positive = coef_corr_positive_by_city(df_dict_Loc)
    coef_corr_negative = coef_corr_negative_by_city(df_dict_Loc)
    for key in df_dict_Loc.keys():
        for i in range(0,features_concat[key][0]):
            if i<=(len(coef_corr_positive[key])-1):
                features[key].append(coef_corr_positive[key].index[i])
            elif i >= len(coef_corr_positive[key]):
                features[key].append(coef_corr_negative[key].index[i-(len(coef_corr_positive[key])+1)])
    return features

def x_features(df_dict_Loc: dict) -> dict:
    features = build_features(df_dict_Loc)
    X = {elem : pd.DataFrame() for elem in Loc}
    for key in df_dict_Loc.keys():
        X[key]= df_dict_Loc[key][features[key]].copy()
    return X


def y_features(df_dict_Loc: dict) -> dict:
    y = {elem : pd.DataFrame() for elem in Loc}
    for key in df_dict_Loc.keys():
        y[key]= df_dict_Loc[key][['RainTomorrow']].copy()
    return y