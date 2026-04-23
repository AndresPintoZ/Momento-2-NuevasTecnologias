import pandas as pd
from carga import cargar_comercio, cargar_categoria
from limpieza import limpiar_datos_comercio, Limpiar_datos_categoria

def analizar_comercio(df_comercio):
    print("\n===== ANÁLISIS DE COMERCIO =====")
    print("Total registros:", len(df_comercio))
    print("Ciudades únicas:", df_comercio['ciudad'].nunique())
    print("Top 5 ciudades con más registros:")
    print(df_comercio['ciudad'].value_counts().head())
    print("\nTop 5 actividades más frecuentes:")
    print(df_comercio['actividad'].value_counts().head())

def analizar_categoria(df_categoria):
    print("\n===== ANÁLISIS DE CATEGORÍA =====")
    print("Total categorías:", len(df_categoria))
    print("Estados únicos:", df_categoria['estado'].unique())
    print("\nTop 5 categorías más frecuentes:")
    print(df_categoria['Nombre'].value_counts().head())

if __name__ == "__main__":
    
    df_comercio = cargar_comercio()
    df_categoria = cargar_categoria()

    # Limpiar
    df_comercio = limpiar_datos_comercio(df_comercio)
    df_categoria = Limpiar_datos_categoria (df_categoria)

    analizar_comercio(df_comercio)
    analizar_categoria(df_categoria)

import pandas as pd

# Función de análisis para Gastos Limpios-------------------------------------------------------------------------------------- 
def analizar_Gastos_Limpios(df_Gastos_Limpios):

    # Análisis de Categorías............................................................................
    #saber cuantas categorias existen
    print("Cantidad de categorías únicas:")
    print(df_Gastos_Limpios['categoria'].nunique())

    # Cuánto se gasta por categoría
    print("Gasto por categoría:")
    print(df_Gastos_Limpios.groupby("categoria")["valor"].sum().sort_values(ascending=False))

    # Cuántas transacciones por categoría
    print("Transacciones por categoría:")
    print(df_Gastos_Limpios.groupby("categoria")["valor"].count())

    # Análisis de Valores..............................................................................
    print("Análisis de valores:")
    print(df_Gastos_Limpios.describe())
    print("Gasto promedio:")
    print(df_Gastos_Limpios["valor"].mean())
    print("Gasto total:")
    print(df_Gastos_Limpios["valor"].sum())
    print("Máximo gasto:")
    print(df_Gastos_Limpios["valor"].max())
    print("Mínimo gasto:")
    print(df_Gastos_Limpios["valor"].min())

    # Análisis de Fechas...............................................................................
    print("Análisis de fechas:")
    print(df_Gastos_Limpios["fecha"].min())
    print(df_Gastos_Limpios["fecha"].max())

    # Análisis de Medios de Pago.......................................................................
    print("Análisis de medios de pago:")
    print(df_Gastos_Limpios["medioPago"].value_counts())

    # Análisis de Comercios.............................................................................
    print("Análisis de comercios:")
    print(df_Gastos_Limpios["comercio"].value_counts())

    # Análisis de Estados.............................................................................
    print("Análisis de estados:")
    print(df_Gastos_Limpios["estado"].value_counts())

    # Análisis de Notas..............................................................................
    print("Análisis de notas:")
    print(df_Gastos_Limpios["notas"].value_counts())

    return df_Gastos_Limpios



