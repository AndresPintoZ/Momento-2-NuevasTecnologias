# Limpieza de Datos con Python

Este proyecto está enfocado en el proceso de **Data Cleaning** (Limpieza de Datos), una etapa crítica en cualquier flujo de trabajo de ciencia de datos. El objetivo es transformar datos crudos en un conjunto de datos limpio, consistente y listo para el análisis o modelado.

## Descripción del Proyecto

El proyecto incluye scripts y notebooks diseñados para abordar problemas comunes en los datasets, tales como:
- Manejo de valores faltantes (missing values).
- Eliminación de registros duplicados.
- Estandarización de formatos (fechas, textos, categorías).
- Detección y tratamiento de valores atípicos (outliers).
- Conversión de tipos de datos.

## Requisitos Previos

Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior**: Puedes descargarlo desde [python.org](https://www.python.org/).
- **Gestor de paquetes pip**: Generalmente incluido con la instalación de Python.

## Instalación y Configuración

Sigue estos pasos para configurar tu entorno local:

1. **Clonar el repositorio** :
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-directorio>
   ```

2. **Crear un entorno virtual** :
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`

4. **Instalar las dependencias**:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

## Ejecución

Para iniciar el proceso de limpieza, puedes ejecutar el script principal:

```bash
python main.py
```
