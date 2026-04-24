import pandas as pd
from carga import cargar_comercio, cargar_categoria, cargar_Usuarios
from limpieza import limpiar_datos_comercio, Limpiar_datos_categoria, limpiar_Datos_Usuarios

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


# Función de análisis para Usuarios Limpios------------------------------------------------------------------------------------
def analizar_Usuarios_Limpios(df_Usuarios_Limpios):

    print("\n" + "=" * 55)
    print("  ANÁLISIS DE DATOS DE LA ENTIDAD USUARIOS")
    print("=" * 55)

    # ── ¿Cuál ciudad tiene mayor cantidad de usuarios registrados? ───────────────────────
    print("\n" + "─" * 55)
    print("Frecuencia por Ciudad")
    print("─" * 55 + "\n")

    conteo_ciudades = df_Usuarios_Limpios['ciudad'].value_counts().sort_values(ascending=False)
    ciudad_top      = conteo_ciudades.index[0]
    cantidad_top    = conteo_ciudades.iloc[0]

    print(f"  Ciudad con más usuarios: '{ciudad_top}' con {cantidad_top} usuarios\n")
    print("  Distribución completa:")
    for ciudad, cantidad in conteo_ciudades.items():
        print(f"    {ciudad:<20} - {cantidad} usuario(s)")

    print(f"\n  Ciudades únicas: {df_Usuarios_Limpios['ciudad'].nunique()}")

    # ── ¿Cuál es la edad promedio por ciudad? ────────────────────
    print("\n" + "─" * 55)
    print("Edad Promedio por Ciudad")
    print("─" * 55 + "\n")

    edad_promedio = (
        df_Usuarios_Limpios.groupby('ciudad')['edad']
        .mean()
        .round(1)
        .sort_values(ascending=False)
    )
    for ciudad, promedio in edad_promedio.items():
        print(f"    {ciudad:<20} - {promedio} años")

    print(f"\n  Edad promedio global : {round(df_Usuarios_Limpios['edad'].mean(), 1)} años")
    print(f"  Edad máxima          : {df_Usuarios_Limpios['edad'].max()} años")
    print(f"  Edad mínima          : {df_Usuarios_Limpios['edad'].min()} años")

    # ── ¿Cuántos usuarios están en estado activo? ───────────────────
    print("\n" + "─" * 55)
    print("Usuarios en Estado Activo")
    print("─" * 55 + "\n")

    conteo_estados   = df_Usuarios_Limpios['estado'].value_counts()
    total            = len(df_Usuarios_Limpios)
    activos          = df_Usuarios_Limpios[df_Usuarios_Limpios['estado'] == 'Activo'].shape[0]
    inactivos        = df_Usuarios_Limpios[df_Usuarios_Limpios['estado'] == 'Inactivo'].shape[0]
    otros            = total - activos - inactivos

    print(f"  Activos   : {activos}")
    print(f"  Inactivos : {inactivos}")
    print(f"  Otros     : {otros}")
    print(f"  Total       : {total}")

    # ── "¿Cuántos usuarios son mayores de 18 años? ──────────────────────
    print("\n" + "─" * 55)
    print("Usuarios Mayores de 18 Años")
    print("─" * 55 + "\n")

    mayores_18 = df_Usuarios_Limpios[df_Usuarios_Limpios['edad'] > 18]
    pct        = round(mayores_18.shape[0] / total * 100, 1)

    print(f"  Usuarios mayores de 18 años : {mayores_18.shape[0]}")
    print(f"  Porcentaje sobre el total   : {pct}%")

    # ── "¿Cuántos correos fueron corregidos durante la limpieza? ────────
    print("\n" + "─" * 55)
    print("Calidad de Datos: Correos Corregidos")
    print("─" * 55 + "\n")

    correos_corregidos  = df_Usuarios_Limpios['correo'].str.contains('@corregido.com', na=False).sum()
    correos_validos     = df_Usuarios_Limpios['correo'].str.contains(r'@\w+\.\w+', regex=True, na=False).sum()

    print(f"  Correos marcados como '@corregido.com' : {correos_corregidos}")
    print(f"  Correos con formato válido final       : {correos_validos}")

    # ── Tipos de Documento y País ────────────────────────
    print("\n" + "─" * 55)
    print("Tipos de Documento y País")
    print("─" * 55 + "\n")

    print("\n  Distribución por tipo de documento:")
    for tipo, cant in df_Usuarios_Limpios['tipoDocumento'].value_counts().items():
        print(f"    {tipo:<10} - {cant} usuario(s)")

    print("\n  Distribución por país:")
    for pais, cant in df_Usuarios_Limpios['pais'].value_counts().items():
        print(f"    {pais:<20} - {cant} usuario(s)")

    return df_Usuarios_Limpios

if __name__ == "__main__":

    df_Usuarios = cargar_Usuarios()
    df_Usuarios_Limpios = limpiar_Datos_Usuarios(df_Usuarios)

    analizar_Usuarios_Limpios(df_Usuarios_Limpios)

