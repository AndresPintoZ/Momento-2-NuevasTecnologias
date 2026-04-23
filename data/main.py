import carga
import limpieza
import analisis

#Gastos Sucios......................................................................................

print('Proceso de Carga')
df_Gastos = carga.cargar_Gastos()

print('Proceso de Limpieza')
df_Gastos = limpieza.limpiar_Datos_Gastos(df_Gastos)


#Gastos Limpios......................................................................................

print('Proceso de Carga de Datos Limpios')
df_Gastos_Limpios = carga.Cargar_Gastos_Limpios()

print('Proceso de Análisis')
df_Gastos_Limpios = analisis.analizar_Gastos_Limpios(df_Gastos_Limpios)
