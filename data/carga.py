from numpy import int64
import pandas as pd

def cargar_Gastos():
    # Usamos skipinitialspace=True para eliminar los espacios después de las comas en el encabezado
    df_Gastos = pd.read_csv('data/row/Gastos_Sucios.csv', skipinitialspace=True)
    df_Gastos.info()
    return df_Gastos