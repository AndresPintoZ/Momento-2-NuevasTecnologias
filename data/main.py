import carga
import limpieza
import analisis
import pandas as pd

while True:
    print("\n" + "="*30)
    print("   MENÚ DE GESTIÓN DE DATOS")
    print("="*30)
    print("1. Limpiar todos los datos (Gastos, Comercio, Categorías)")
    print("2. Ver análisis de Gastos")
    print("3. Ver análisis de Comercio y Categorías")
    print("4. Salir")
    print("="*30)
    
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print('\n--- Iniciando Proceso de Limpieza ---')
        # Limpieza de Gastos
        df_gastos_raw = carga.cargar_Gastos()
        limpieza.limpiar_Datos_Gastos(df_gastos_raw)
        
        # Limpieza de Comercio y Categoría
        df_comercio_raw = carga.cargar_comercio()
        df_categoria_raw = carga.cargar_categoria()
        limpieza.limpiar_datos_comercio(df_comercio_raw)
        limpieza.Limpiar_datos_categoria(df_categoria_raw)
        print("\n¡Todos los archivos han sido limpiados y guardados en /processed/!")

    elif opcion == "2":
        print('\n--- Análisis de Gastos ---')
        try:
            df_Gastos_Limpios = carga.Cargar_Gastos_Limpios()
            analisis.analizar_Gastos_Limpios(df_Gastos_Limpios)
        except:
            print("Error: Primero debes ejecutar la opción 1 para limpiar los datos.")

    elif opcion == "3":
        print('\n--- Análisis de Comercio y Categoría ---')
        try:
            df_comercio = pd.read_csv('data/processed/comercio_limpio.csv')
            df_categoria = pd.read_csv('data/processed/categoria_limpio.csv')
            analisis.analizar_comercio(df_comercio)
            analisis.analizar_categoria(df_categoria)
        except:
            print("Error: No se encuentran los archivos limpios. Ejecuta la opción 1 primero.")

    elif opcion == "4":
        print("Saliendo del programa... ¡Adiós!")
        break  # Aquí termina el bucle "do-while"
    else:
        print("Opción no válida, por favor intenta de nuevo.")
