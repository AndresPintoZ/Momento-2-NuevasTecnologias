import pandas as pd 

def limpiar_datos(df_comercioComercio):
    print("Limpiando datos...")
    # Eliminar filas con valores faltantes
    df_comercioComercio['nombre'] = df_comercioComercio['nombre'].str.strip().str.title()
    df_comercioComercio['direccion'] = df_comercioComercio['direccion'].str.strip().str.title()
    df_comercioComercio['telefono'] = df_comercioComercio['telefono'].str.strip()
    df_comercioComercio['nit']=df_comercioComercio['nit'].str.strip()
    df_comercioComercio['actividad']=df_comercioComercio['actividad'].str.strip().str.title()