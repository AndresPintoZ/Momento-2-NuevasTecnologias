import carga
import limpieza

print('Proceso de Carga')
df_Gastos = carga.cargar_Gastos()
df_Gastos = limpieza.limpiar_Datos_Gastos(df_Gastos)
