import pandas as pd

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



