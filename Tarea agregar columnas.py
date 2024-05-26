#Para esta tarea voy a generar los datos de sciencescore de forma aleatoria para agregar esta columna al csv.

import pandas as pd
from random import randint

# Leer el archivo CSV
file_path = "C:/Users/Lalita/Desktop/ML_Diana/Datos puntajes alumnos.csv"
df = pd.read_csv(file_path)

# Generar 4437 calificaciones aleatorias en el rango de 0 a 100
sciencescore = [randint(0, 100) for _ in range(4437)]

# Agregar una nueva columna 'Calificaciones' al DataFrame
df['sciencescore'] = sciencescore

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('datos_actualizados.csv', index=False)

#Aquí se filtrarán los datos en los que el score de matemáticaas sea mayor o igual a 90:
# Filtrar datos donde las calificaciones sean mayores o iguales a 90
resultados_filtrados_mathscore = df[df['MathScore'] >= 90]

# Imprimir los resultados filtrados
print(resultados_filtrados_mathscore)

#Aquí se creará el subconjunto de alumnas:
# Crear un subconjunto con los datos de alumnas mujeres
alumnas = df[df['Gender'] == 'female']

# Imprimir el subconjunto
print(alumnas)
