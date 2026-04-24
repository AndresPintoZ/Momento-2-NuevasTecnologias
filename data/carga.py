import pandas as pd


#carga de Comercio y Categoria--------------------------------------------------------------------------------------
def cargar_comercio ():
    df_comercioComercio=pd.read_csv('data/row/comercio.csv')
    df_comercioComercio.info()
    return df_comercioComercio

def cargar_categoria():
    df_categoria=pd.read_csv('data/row/categoria.csv')
    df_categoria.info()
    return df_categoria

#carga de Gastos Sucios y Limpios--------------------------------------------------------------------------------------
def cargar_Gastos():
    df_Gastos = pd.read_csv('data/row/Gastos_Sucios.csv')
    df_Gastos.info()
    return df_Gastos

def Cargar_Gastos_Limpios():
    df_Gastos_Limpios = pd.read_csv('data/processed/Gastos_Limpios.csv')
    df_Gastos_Limpios.info()
    return df_Gastos_Limpios


#carga de Usuarios Sucios y Limpios--------------------------------------------------------------------------------------
def cargar_Usuarios():
    df_Usuarios = pd.read_csv('data/row/Usuarios_Sucios.csv')
    df_Usuarios.info()
    return df_Usuarios

def Cargar_Usuarios_Limpios():
    df_Usuarios_Limpios = pd.read_csv('data/processed/Usuarios_Limpios.csv')
    df_Usuarios_Limpios.info()
    return df_Usuarios_Limpios
