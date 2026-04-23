
import pandas as pd

def cargar_comercio ():
    df_comercioComercio=pd.read_csv('./row/comercio.csv')
    df_comercioComercio.info()
   
    return df_comercioComercio

def cargar_categoria():
    df_categoria=pd.read_csv('./row/categoria.csv')
    df_categoria.info()

    return df_categoria