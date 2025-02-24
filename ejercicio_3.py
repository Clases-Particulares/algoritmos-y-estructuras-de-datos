# Dada una matriz de enteros (de dimensiones m x n), desarrolla un programa que:

# Calcule la suma de cada fila y la suma de cada columna.
# Imprima la fila con la mayor suma y la columna con la menor suma.

import random

matriz = []

columnas = random.randint(1, 10)
filas = random.randint(1, 10)

# carga la matriz de números aleatoriamente
for i in range(filas):
  fila = []
  for j in range(columnas):
    fila.append(random.randint(0, 1000))
  matriz.append(fila)

# calcula la suma de cada fila
suma_filas = []
for i in range(len(matriz)):
  suma_fila = 0
  for columna in matriz[i]:
    suma_fila += columna
  suma_filas.append(suma_fila)

# calcula la suma de cada columna
suma_columnas = []
for j in range(columnas):
  suma_columna = 0
  for i in range(filas):
    suma_columna += matriz[i][j]
  suma_columnas.append(suma_columna)


# imprime la mayor suma de todas las filas
mayor = suma_filas[0]
indice_fila = 0
for i in range(len(suma_filas)):
  if mayor < suma_filas[i]:
    mayor = suma_filas[i]
    indice_fila = i

print("La fila con mayor suma es", indice_fila + 1, "con", mayor)

# imprime la menor suma de todas las columnas

menor = suma_columnas[0]
indice_columna = 0
for i in range(len(suma_columnas)):
  if suma_columnas[i] < menor:
    menor = suma_columnas[i]

print("La columna con la menor suma es", indice_columna + 1, "con", menor)

[print(fila) for fila in matriz]
