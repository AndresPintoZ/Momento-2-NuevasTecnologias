import pandas as pd

def limpiar_datos_comercio(df_comercioComercio):
    print("Limpiando datos...")

    # Primero convertir a string las columnas que pueden ser numéricas
    df_comercioComercio['id'] = df_comercioComercio['id'].astype(str).str.strip().str.title()
    df_comercioComercio['nit'] = df_comercioComercio['nit'].astype(str).str.strip().str.title()
    df_comercioComercio['id_cliente'] = df_comercioComercio['id_cliente'].astype(str).str.strip().str.title()

    # Limpieza de columnas de texto
    df_comercioComercio['nombre'] = df_comercioComercio['nombre'].astype(str).str.strip().str.title()
    df_comercioComercio['direccion'] = df_comercioComercio['direccion'].astype(str).str.strip().str.title()
    df_comercioComercio['telefono'] = df_comercioComercio['telefono'].astype(str).str.strip()
    df_comercioComercio['actividad'] = df_comercioComercio['actividad'].astype(str).str.strip().str.title()
    df_comercioComercio['contacto'] = df_comercioComercio['contacto'].astype(str).str.strip().str.title()
    df_comercioComercio['telefono'] = df_comercioComercio['telefono'].astype(str).str.strip().str.title()
    df_comercioComercio['direccion'] = df_comercioComercio['direccion'].astype(str).str.strip().str.title()

    print('Eliminando datos duplicados')
    df_comercioComercio = df_comercioComercio.drop_duplicates()

    # Validaciones
    ciudades_Validas = [
        "Medellin","Bogotá","Cali","Cartagena","Barranquilla","Santa Marta",
        "Cúcuta","Villavicencio","Pereira","Popayán","Tunja","Sincelejo",
        "Montería","Riohacha","Valledupar","Pasto","Quibdó","Leticia",
        "Florencia","San Andrés","Neiva"
    ]

    tiendas_validas = [
        "Supermercado Exito","Alkosto","Tiendas Olímpica","Postobon","Bavaria",
        "Almacen La 14","Supertiendas Cañaveral","Almacen Metro","Almacen Carulla",
        "Almacen D1","Almacen Justo&Bueno","Almacen Ara","Makro"
    ]
    
    mascara_ciudad = df_comercioComercio['ciudad'].isin(ciudades_Validas)
    mascara_tienda = df_comercioComercio['nombre'].isin(tiendas_validas)
    erroresDetectados = df_comercioComercio[~(mascara_ciudad & mascara_tienda)]

    print("Registros con errores detectados:")
    print(erroresDetectados)

    # Reemplazos y nulos
    df_comercioComercio['pais'] = df_comercioComercio['pais'].replace({'Colómbia':'Colombia'})
    df_comercioComercio['id']        = df_comercioComercio['id'].fillna("0")
    df_comercioComercio['nit']       = df_comercioComercio['nit'].fillna("000000000")
    df_comercioComercio['nombre']    = df_comercioComercio['nombre'].fillna("Desconocido")
    df_comercioComercio['actividad'] = df_comercioComercio['actividad'].fillna("No Definida")
    df_comercioComercio['contacto']  = df_comercioComercio['contacto'].fillna("Sin Contacto")
    df_comercioComercio['telefono']  = df_comercioComercio['telefono'].fillna("00000000")
    df_comercioComercio['direccion'] = df_comercioComercio['direccion'].fillna("Sin Dirección")
    df_comercioComercio['ciudad']    = df_comercioComercio['ciudad'].fillna("Desconocida")
    df_comercioComercio['pais']      = df_comercioComercio['pais'].fillna("Colombia")

    # Correcciones específicas
    df_comercioComercio['telefono']  = df_comercioComercio['telefono'].replace("Abc123", "00000000")
    df_comercioComercio['pais']      = df_comercioComercio['pais'].replace({"Pais ":"Colombia","Pais A":"Colómbia"})

    # Convertir de nuevo a numérico
    df_comercioComercio['nit'] = pd.to_numeric(df_comercioComercio['nit'], errors='coerce').fillna(0).astype(int)
    df_comercioComercio['id']  = pd.to_numeric(df_comercioComercio['id'], errors='coerce').fillna(0).astype(int)
    df_comercioComercio['id_cliente']  = pd.to_numeric(df_comercioComercio['id_cliente'], errors='coerce').fillna(0).astype(int)

    df_comercioComercio.to_csv('.//processed/comercio_limpio.csv', index=False)
    return df_comercioComercio


import pandas as pd
import os

def Limpiar_datos_categoria(df_categoria):
    print("Limpiando datos de categoría...")

    # Convertir columnas numéricas a string para poder usar .str
    df_categoria['id'] = df_categoria['id'].astype(str).str.strip().str.title()
    df_categoria['id_cliente'] = df_categoria['id_cliente'].astype(str).str.strip().str.title()

    # Limpieza de columnas de texto
    df_categoria['Nombre'] = df_categoria['Nombre'].astype(str).str.strip().str.title()
    df_categoria['fecha de creación'] = df_categoria['fecha de creación'].astype(str).str.strip().str.title()
    df_categoria['fecha de modificación'] = df_categoria['fecha de modificación'].astype(str).str.strip().str.title()
    df_categoria['usuarioDecreacion'] = df_categoria['usuarioDecreacion'].astype(str).str.strip().str.title()
    df_categoria['usuarioDemodificacion'] = df_categoria['usuarioDemodificacion'].astype(str).str.strip().str.title()
    df_categoria['estado'] = df_categoria['estado'].astype(str).str.strip().str.title()

    # Eliminar duplicados
    df_categoria = df_categoria.drop_duplicates()

    # Reemplazar valores nulos
    df_categoria['id'] = df_categoria['id'].fillna("0")
    df_categoria['Nombre'] = df_categoria['Nombre'].fillna("Desconocido")
    df_categoria['fecha de creación'] = df_categoria['fecha de creación'].fillna("Sin Fecha")
    df_categoria['fecha de modificación'] = df_categoria['fecha de modificación'].fillna("Sin Fecha")
    df_categoria['usuarioDecreacion'] = df_categoria['usuarioDecreacion'].fillna("Sin Usuario")
    df_categoria['usuarioDemodificacion'] = df_categoria['usuarioDemodificacion'].fillna("Sin Usuario")
    df_categoria['estado'] = df_categoria['estado'].fillna("Desconocido")
    df_categoria['id_cliente'] = df_categoria['id_cliente'].fillna("0")

    # Convertir de nuevo a numérico
    df_categoria['id'] = pd.to_numeric(df_categoria['id'], errors='coerce').fillna(0).astype(int)
    df_categoria['id_cliente'] = pd.to_numeric(df_categoria['id_cliente'], errors='coerce').fillna(0).astype(int)

    df_categoria.to_csv("./processed/categoria_limpio.csv", index=False)

    return df_categoria
