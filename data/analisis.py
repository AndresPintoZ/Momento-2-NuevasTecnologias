
import pandas as pd

def mostrarCategoriaF(df_categoriaFila):
    df_categoriaFila= pd.read_csv('./datta/raw/categoria_limpio.csv', sep=',')

    print(df_categoriaFila.head(5))

def mostrarComercioF(df_comercioFila ):
    df_comercioFila= pd.read_csv('./datta/raw/comercio_limpio.csv', sep=',')

    print(df_comercioFila.head(5))
