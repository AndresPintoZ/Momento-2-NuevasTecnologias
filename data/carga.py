from numpy import int64
import pandas as pd

def cargar_Gastos():
    df_Gastos = pd.read_csv('data/row/Gastos_Sucios.csv')
    df_Gastos.info()
    return df_Gastos