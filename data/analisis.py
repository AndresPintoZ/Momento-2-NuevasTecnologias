import pandas as pd
from carga import cargar_comercio, cargar_categoria, cargar_pagos
from limpieza import limpiar_datos_comercio, Limpiar_datos_categoria, limpiar_datos_pagos

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

    df_pagos = cargar_pagos()
    df_pagos = limpiar_datos_pagos(df_pagos)

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

# Análisis de Pagos
def analizar_pagos(df_pagos):
    """Analizar datos de pagos"""
    print("\n" + "="*50)
    print("===== ANÁLISIS DE PAGOS =====")
    print("="*50)
    
    print(f"\nTotal registros: {len(df_pagos)}")
    
    # Estado de pagos
    print("\nDistribución por estado:")
    print(df_pagos['estado'].value_counts())
    
    # Método de pago
    print("\nDistribución por método de pago:")
    print(df_pagos['metodo_pago'].value_counts())
    
    # Monto total y promedio
    print(f"\nMonto total: ${df_pagos['monto'].sum():,.2f}")
    print(f"Monto promedio: ${df_pagos['monto'].mean():,.2f}")
    print(f"Monto máximo: ${df_pagos['monto'].max():,.2f}")
    print(f"Monto mínimo: ${df_pagos['monto'].min():,.2f}")
    
    # Productos más frecuentes
    print("\nTop 5 productos más frecuentes:")
    print(df_pagos['producto'].value_counts().head())
    
    print("\n" + "="*60)
    print("RESPUESTAS A PREGUNTAS DE ANÁLISIS")
    print("="*60)
    
    #¿Cuál es el producto con más registros?
    print("\n--- 1. ANÁLISIS DE FRECUENCIA ---")
    print("¿Cuál es el producto con la mayor cantidad de registros?")
    producto_mas_frecuente = df_pagos['producto'].value_counts().idxmax()
    cantidad_max = df_pagos['producto'].value_counts().max()
    print(f"→ Producto: {producto_mas_frecuente}")
    print(f"→ Cantidad de registros: {cantidad_max}")
    
    #Análisis de Agregación: Calcular métrica agrupada por categoría
    print("\n--- 2. ANÁLISIS DE AGRUPACIÓN ---")
    print("¿Cuál es el monto total y promedio por método de pago?")
    agrupacion = df_pagos.groupby('metodo_pago').agg({
        'monto': ['sum', 'mean', 'count']
    }).round(2)
    agrupacion.columns = ['Monto Total', 'Monto Promedio', 'Cantidad']
    print(agrupacion.to_string())
    
    #Análisis con Filtrado y Conteo: Segmentar y contar
    print("\n--- 3. ANÁLISIS CON FILTRADO Y CONTEO ---")
    
    # Pagos en estado "Fallido"
    pagos_fallidos = df_pagos[df_pagos['estado'] == 'Fallido']
    print(f"¿Cuántos pagos están en estado 'Fallido'?")
    print(f"→ Cantidad: {len(pagos_fallidos)}")
    
    # Pagos en estado "Completado"
    pagos_completados = df_pagos[df_pagos['estado'] == 'Completado']
    print(f"\n¿Cuántos pagos están en estado 'Completado'?")
    print(f"→ Cantidad: {len(pagos_completados)}")
    
    # Pagos en estado "Pendiente"
    pagos_pendientes = df_pagos[df_pagos['estado'] == 'Pendiente']
    print(f"\n¿Cuántos pagos están en estado 'Pendiente'?")
    print(f"→ Cantidad: {len(pagos_pendientes)}")
    
    # Montos mayores a $5000
    pagos_altos = df_pagos[df_pagos['monto'] > 5000]
    print(f"\n¿Cuántos pagos tienen monto mayor a $5,000?")
    print(f"→ Cantidad: {len(pagos_altos)}")
    print(f"→ Monto total de pagos altos: ${pagos_altos['monto'].sum():,.2f}")
    
    analizar_pagos(df_pagos)

    return df_pagos

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




