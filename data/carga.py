from numpy import int64
import pandas as pd

def cargar_Gastos():
    df_Gastos = pd.read_csv('data/row/Gastos_Sucios.csv')
    df_Gastos.info()
    return df_Gastos

def Cargar_Gastos_Limpios():
    df_Gastos_Limpios = pd.read_csv('data/prosecced/Gastos_Limpios.csv')
    df_Gastos_Limpios.info()
    return df_Gastos_Limpios