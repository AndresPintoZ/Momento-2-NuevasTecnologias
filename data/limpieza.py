import pandas as pd

def limpiar_datos_comercio(df_comercioComercio):
    print("Limpiando datos...")

    df_comercioComercio['id'] = df_comercioComercio['id'].str.strip().str.title()
    df_comercioComercio['nombre'] = df_comercioComercio['nombre'].str.strip().str.title()
    df_comercioComercio['direccion'] = df_comercioComercio['direccion'].str.strip().str.title()
    df_comercioComercio['telefono'] = df_comercioComercio['telefono'].str.strip()
    df_comercioComercio['nit']=df_comercioComercio['nit'].str.strip().str.title()
    df_comercioComercio['actividad']=df_comercioComercio['actividad'].str.strip().str.title()
    df_comercioComercio['contacto']=df_comercioComercio['contacto'].str.strip().str.title()
    df_comercioComercio['teléfono']=df_comercioComercio['teléfono'].str.strip().str.title()
    df_comercioComercio['dirección']=df_comercioComercio['dirección'].str.strip().str.title()

    print('Eliminando datos duplicadoe')
    df_comercioComercio=df_comercioComercio.drop_duplicates()

    print('.....................')

    ciudades_Validas= [
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

    paises_dicionario = {'Colombia','Colómbia'}
    df_comercioComercio['pais']=df_comercioComercio['pais'].replace(paises_dicionario)

    print("replazando nulos valores nulos")
    df_comercioComercio['id']        = df_comercioComercio['id'].fillna("0")
    df_comercioComercio['nit']       = df_comercioComercio['nit'].fillna("000000000")
    df_comercioComercio['nombre']    = df_comercioComercio['nombre'].fillna("Desconocido")
    df_comercioComercio['actividad'] = df_comercioComercio['actividad'].fillna("No Definida")
    df_comercioComercio['contacto']  = df_comercioComercio['contacto'].fillna("Sin Contacto")
    df_comercioComercio['telefono']  = df_comercioComercio['telefono'].fillna("00000000")
    df_comercioComercio['dirección'] = df_comercioComercio['dirección'].fillna("Sin Dirección")
    df_comercioComercio['ciudad']    = df_comercioComercio['ciudad'].fillna("Desconocida")
    df_comercioComercio['país']      = df_comercioComercio['país'].fillna("Colombia")

    df_comercioComercio['telefono']  = df_comercioComercio['telefono'].replace("Abc123", "00000000")
    df_comercioComercio['país']      = df_comercioComercio['país'].replace("País ", "Colombia")
    df_comercioComercio['país']      = df_comercioComercio['país'].replace("País A", "Colómbia")

    df_comercioComercio['nit'] = pd.to_numeric(df_comercioComercio['nit'], errors='coerce').fillna(0).astype(int)
    df_comercioComercio['id']  = pd.to_numeric(df_comercioComercio['id'], errors='coerce').fillna(0).astype(int)

    df_comercioComercio.to_csv('../datta/processed/comercio_limpio.csv', index=False)


def Limpiar_datos_categoria(df_categoria):
    df_categoria['id']=df_categoria['id'].str.strip().str.title()
    df_categoria['Nombre']=df_categoria['Nombre'].str.strip().str.title()
    df_categoria['fecha de creación']=df_categoria['fecha de creación'].str.strip().str.title()
    df_categoria['fecha de modificación']=df_categoria['fecha de modificación'].str.strip().str.title()
    df_categoria['usuarioDecreacion']=df_categoria['usuarioDecreacion'].str.strip().str.title()
    df_categoria['usuarioDemodificacion']=df_categoria['usuarioDemodificacion'].str.strip().str.title()
    df_categoria['estado']=df_categoria['estado'].str.strip().str.title()

    df_categoria=df_categoria.drop_duplicates()

   
    df_categoria['id']                   = df_categoria['id'].fillna("0")
    df_categoria['Nombre']               = df_categoria['Nombre'].fillna("Desconocido")
    df_categoria['fecha de creación']    = df_categoria['fecha de creación'].fillna("Sin Fecha")
    df_categoria['fecha de modificación']= df_categoria['fecha de modificación'].fillna("Sin Fecha")
    df_categoria['usuarioDecreacion']    = df_categoria['usuarioDecreacion'].fillna("Sin Usuario")
    df_categoria['usuarioDemodificacion']= df_categoria['usuarioDemodificacion'].fillna("Sin Usuario")
    df_categoria['estado']               = df_categoria['estado'].fillna("Desconocido")

    df_categoria['id']  = pd.to_numeric(df_categoria['id'], errors='coerce').fillna(0).astype(int)


    df_categoria.to_csv('../datta/processed/categoria_limpio.csv', index=False)