import pandas as pd

def limpiar_Datos_Gastos(df_Gastos):

    # Eliminación de Duplicados.......................................................................
    print(f"Cantidad de registros antes de eliminar duplicados: {len(df_Gastos)}")
    df_Gastos = df_Gastos.drop_duplicates()

    #limpieza de espacios en blanco y estandarización de mayúsculas...................................
    print("Limpiando espacios en blanco y estandarizando mayúsculas")
    df_Gastos['descripcion'] = df_Gastos['descripcion'].str.strip().str.title()
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
    lista_estricta_Gastos = ['Alimentos',  'Ayuntamiento', 'Entretenimiento', 'Servicios', 'Salud', 'Educación', 'Ropa', 'Vivienda', 'Tecnología', 'Otros', 'Viajes']

    # Usamos ~ (NOT) para buscar a los que violan la regla de la lista estricta.......................
    print("Verificación de Categorías Lógicas")
    mas_violaciones = ~df_Gastos['categoria'].isin(lista_estricta_Gastos)
    errores_Gastos = df_Gastos[mas_violaciones]

    print("Gastos con categorías que no están en la lista estricta:")
    print(errores_Gastos)
    
    # Guardamos el DataFrame limpio en un nuevo archivo CSV...........................................
    df_Gastos.to_csv('data/prosecced/Gastos_Limpios.csv', index=False)
    
