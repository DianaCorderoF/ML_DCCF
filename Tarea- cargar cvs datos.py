import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('C:/Users/Lalita/Desktop/ML_Diana/Datos puntajes alumnos.csv')

# Realizar cualquier manipulación necesaria con pandas
# Por ejemplo, imprimir las primeras filas del DataFrame
print(df.head())

# Guardar el DataFrame como un archivo CSV en el repositorio clonado
df.to_csv('C:/Users/Lalita/Desktop/ML_Diana/Datos puntajes alumnos.csv', index=False)
pd.set_option('display.max_rows', None)  # Mostrar todas las filas
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas

# Mostrar el DataFrame completo
print(df)
# En estos datos, la columna "gender" es binaria (female/male), igual que la columna "lunchtype" (standard/reduced) y 
#testprep (none/completed). Las columnas "ethnic group" y "parent education" son columnas con datos discretos
# group A-B-C-D-E para la primera y diferentes opciones de nivel de estudios para la segunda. 
#Por último, las columasn "mathscore", "readingscore" y "writingscore" son variables enteras que muestran la 
#calificación de cada alumno. 
