
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
