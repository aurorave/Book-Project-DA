import pandas as pd
import numpy as np

df = pd.read_csv('alading_week_202211291619.csv')
EEEEEEEEEEEEEEEEEEEEEE

def aladin(df):
    df.drop_duplicates(inplace=True)
    df = df.dropna()
    return df


