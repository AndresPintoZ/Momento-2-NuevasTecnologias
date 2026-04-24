import pandas as pd


# Función de limpieza para Comercio Sucio--------------------------------------------------------------------------------------
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


# Función de limpieza para Categoría--------------------------------------------------------------------------------------  
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


# Función de limpieza para Gastos Sucios--------------------------------------------------------------------------------------
def limpiar_Datos_Gastos(df_Gastos):

    # Eliminación de Duplicados.......................................................................
    print(f"Cantidad de registros antes de eliminar duplicados: {len(df_Gastos)}")
    df_Gastos = df_Gastos.drop_duplicates()

    #limpieza de espacios en blanco y estandarización de mayúsculas...................................
    print("Limpiando espacios en blanco y estandarizando mayúsculas")
    df_Gastos['descripcion'] = df_Gastos['descripcion'].str.strip().str.strip('"').str.strip()
    df_Gastos['fecha'] = df_Gastos['fecha'].str.strip().str.title()
    df_Gastos['fecha'] = df_Gastos['fecha'].str.strip().str.title()
    df_Gastos['valor'] = df_Gastos['valor'].str.strip().str.title()
    df_Gastos['imagen'] = df_Gastos['imagen'].str.strip().str.title()
    df_Gastos['medioPago'] = df_Gastos['medioPago'].str.strip().str.title()
    df_Gastos['categoria'] = df_Gastos['categoria'].str.strip().str.title()
    df_Gastos['comercio'] = df_Gastos['comercio'].str.strip().str.title()
    df_Gastos['estado'] = df_Gastos['estado'].str.strip().str.title()
    df_Gastos['notas'] = df_Gastos['notas'].str.strip().str.title()

    #Conversión de Tipos de Datos.....................................................................
    print("Conversión de tipos de datos")
    df_Gastos['fecha'] = pd.to_datetime(df_Gastos['fecha'], errors='coerce')
    df_Gastos['valor'] = pd.to_numeric(df_Gastos['valor'], errors='coerce')
    
    # Eliminamos símbolos de moneda y comas antes de convertir a número...............................
    print("Eliminación de símbolos de moneda y comas")
    if df_Gastos['valor'].dtype == 'object':
        df_Gastos['valor'] = df_Gastos['valor'].replace(r'[$,]|(?i)cop', '', regex=True)
        df_Gastos['valor'] = pd.to_numeric(df_Gastos['valor'], errors='coerce')

    #Tratamiento de nulos y NaN.......................................................................
    print("Tratamiento de nulos y NaN")
    df_Gastos["fecha"] = df_Gastos["fecha"].fillna("2024-01-01")
    df_Gastos['valor'] = df_Gastos['valor'].fillna(0)
    df_Gastos['descripcion'] = df_Gastos['descripcion'].fillna('Sin descripción')
    df_Gastos['imagen'] = df_Gastos['imagen'].fillna('Sin imagen')
    df_Gastos['medioPago'] = df_Gastos['medioPago'].fillna('Desconocido')
    df_Gastos['categoria'] = df_Gastos['categoria'].fillna('Sin categoría')
    df_Gastos['comercio'] = df_Gastos['comercio'].fillna('Sin comercio')
    df_Gastos['estado'] = df_Gastos['estado'].fillna('Desconocido')
    df_Gastos['notas'] = df_Gastos['notas'].fillna('Sin notas')

    # Verificación de Categorías Lógicas - Definimos la lista ANTES de usarla.........................
    print("Verificación de Categorías Lógicas")
    lista_estricta_Gastos = ['Alimentos',  'Ayuntamiento', 'Transporte', 'Entretenimiento', 'Servicios', 'Salud', 'Educación', 'Ropa', 'Vivienda', 'Tecnología', 'Otros', 'Viajes']

    # Usamos ~ (NOT) para buscar a los que violan la regla de la lista estricta.......................
    print("Verificación de Categorías Lógicas")
    mas_violaciones = ~df_Gastos['categoria'].isin(lista_estricta_Gastos)
    errores_Gastos = df_Gastos[mas_violaciones]

    print("Gastos con categorías que no están en la lista estricta:")
    print(errores_Gastos)
    
    # Guardamos el DataFrame limpio en un nuevo archivo CSV...........................................
    df_Gastos.to_csv('data/processed/Gastos_Limpios.csv', index=False)


# Función de limpieza para Usuarios Sucios--------------------------------------------------------------------------------------
def limpiar_Datos_Usuarios(df_Usuarios):

    # Eliminación de Duplicados.......................................................................
    print(f"Cantidad de registros antes de eliminar duplicados: {len(df_Usuarios)}")
    df_Usuarios = df_Usuarios.drop_duplicates()
    df_Usuarios = df_Usuarios.drop_duplicates(subset='documento', keep='first')
    print(f"Cantidad de registros después de eliminar duplicados: {len(df_Usuarios)}")

    # Limpieza de espacios en blanco y estandarización.................................................
    print("Limpiando espacios en blanco y estandarizando texto")
    df_Usuarios['nombre']        = df_Usuarios['nombre'].str.strip().str.title()
    df_Usuarios['tipoDocumento'] = df_Usuarios['tipoDocumento'].str.strip().str.upper()
    df_Usuarios['documento']     = df_Usuarios['documento'].str.strip()
    df_Usuarios['correo']        = df_Usuarios['correo'].str.strip().str.lower()
    df_Usuarios['telefono']      = df_Usuarios['telefono'].astype(str).str.strip()
    df_Usuarios['direccion']     = df_Usuarios['direccion'].str.strip().str.title()
    df_Usuarios['ciudad']        = df_Usuarios['ciudad'].str.strip().str.title()
    df_Usuarios['pais']          = df_Usuarios['pais'].str.strip().str.title()
    df_Usuarios['estado']        = df_Usuarios['estado'].str.strip().str.title()

    # Conversión de Tipos de Datos.....................................................................
    print("Conversión de tipos de datos")
    df_Usuarios['edad'] = pd.to_numeric(df_Usuarios['edad'], errors='coerce')

    # Eliminación de caracteres extraños en teléfono...................................................
    print("Limpieza de teléfonos")
    df_Usuarios['telefono'] = df_Usuarios['telefono'].str.replace(r'[^\d]', '', regex=True)

    # Eliminación de caracteres no alfanuméricos en documento..........................................
    print("Limpieza de documentos")
    df_Usuarios['documento'] = df_Usuarios['documento'].str.replace(r'[^a-zA-Z0-9]', '', regex=True)

    # Corrección de correos inválidos (sin '@')........................................................
    print("Corrección de correos inválidos")
    def corregir_correo(correo):
        if pd.isna(correo):
            return 'sin_correo@desconocido.com'
        if '@' not in str(correo):
            for dominio in ['gmail', 'hotmail', 'yahoo', 'outlook']:
                if dominio in correo:
                    idx = correo.index(dominio)
                    return correo[:idx] + '@' + correo[idx:]
            return correo + '@corregido.com'
        return correo

    df_Usuarios['correo'] = df_Usuarios['correo'].apply(corregir_correo)

    # Tratamiento de nulos y NaN.......................................................................
    print("Tratamiento de nulos y NaN")
    mediana_edad = int(df_Usuarios['edad'].median())
    df_Usuarios['edad']      = df_Usuarios['edad'].fillna(mediana_edad)
    df_Usuarios['edad']      = df_Usuarios['edad'].astype(int)
    df_Usuarios['nombre']    = df_Usuarios['nombre'].fillna('Sin Nombre')
    df_Usuarios['correo']    = df_Usuarios['correo'].fillna('sin_correo@desconocido.com')
    df_Usuarios['telefono']  = df_Usuarios['telefono'].fillna('Sin Teléfono')
    df_Usuarios['direccion'] = df_Usuarios['direccion'].fillna('Sin Dirección')
    df_Usuarios['ciudad']    = df_Usuarios['ciudad'].fillna('Desconocida')
    df_Usuarios['pais']      = df_Usuarios['pais'].fillna('Desconocido')
    df_Usuarios['estado']    = df_Usuarios['estado'].fillna('Desconocido')

    # Verificación de Estados Lógicos..................................................................
    print("Verificación de Estados Lógicos")
    lista_estricta_Usuarios = ['Activo', 'Inactivo']

    mas_violaciones = ~df_Usuarios['estado'].isin(lista_estricta_Usuarios)
    errores_Usuarios = df_Usuarios[mas_violaciones]

    print("Usuarios con estados que no están en la lista estricta:")
    print(errores_Usuarios[['id', 'nombre', 'estado']])

    # Marcar teléfonos incompletos (menos de 10 dígitos)..............................................
    print("Verificación de teléfonos incompletos")
    mascara_incompleto = (
        df_Usuarios['telefono'].str.len() < 10
    ) & (df_Usuarios['telefono'] != 'Sin Teléfono')
    df_Usuarios.loc[mascara_incompleto, 'telefono'] = 'Teléfono Incompleto'

    # Guardamos el DataFrame limpio en un nuevo archivo CSV...........................................
    df_Usuarios.to_csv('data/processed/Usuarios_Limpios.csv', index=False)

    return df_Usuarios