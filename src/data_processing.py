import os
import pandas as pd

def process_data(df):
    data = df.copy()
    ## Categorizacion de variables.
    data['RainToday'] = (data['RainToday'] == 'Yes')*1
    data['RainTomorrow'] = (data['RainTomorrow'] == 'Yes')*1

    return df