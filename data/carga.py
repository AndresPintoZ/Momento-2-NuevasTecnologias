import pandas as pd

def cargar_comercio ():
    df_comercioComercio=pd.read_csv('data/row/comercio.csv')
    df_comercioComercio.info()
    return df_comercioComercio

def cargar_categoria():
    df_categoria=pd.read_csv('data/row/categoria.csv')
    df_categoria.info()
    return df_categoria

def cargar_Gastos():
    df_Gastos = pd.read_csv('data/row/Gastos_Sucios.csv')
    df_Gastos.info()
    return df_Gastos

def Cargar_Gastos_Limpios():
    df_Gastos_Limpios = pd.read_csv('data/processed/Gastos_Limpios.csv')
    df_Gastos_Limpios.info()
    return df_Gastos_Limpios

