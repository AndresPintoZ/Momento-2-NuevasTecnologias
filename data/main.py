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


print("\n\n" + "─" * 55)
print("USUARIOS")
print("─" * 55 + "\n")
# Usuarios Sucios....................................................................................

print('Proceso de Carga')
df_Usuarios = carga.cargar_Usuarios()

print('Proceso de Limpieza')
df_Usuarios = limpieza.limpiar_Datos_Usuarios(df_Usuarios)

# Usuarios Limpios...................................................................................

print('Proceso de Carga de Datos Limpios')
df_Usuarios_Limpios = carga.Cargar_Usuarios_Limpios()

print('Proceso de Análisis')
df_Usuarios_Limpios = analisis.analizar_Usuarios_Limpios(df_Usuarios_Limpios)
