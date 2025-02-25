# Matriz: es un arreglo de dimensiones m x n que contiene elementos de un mismo tipo de dato
# Donde:
# m: número de filas
# n: número de columnas

# Una matriz de 3x3 de enteros se vería algo así
matriz_integer = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# Una matriz 2x3 de strings se vería algo así
matriz_string = [ 
  ["hola", "mundo", "python"],
  ["uno", "dos", "tres"]
]

# Operaciones básicas

# 1. Agregar elementos
matriz_integer.append(
  [10, 11, 12] # Agregamos una fila
)

# 2. Quitar elementos

matriz_integer.remove(
  [10, 11, 12] # Quitamos la fila que agregamos
)

# 3. Modificar elementos

# Accede a la primera fila y modifica el primer elemento
matriz_string[0] = ["adiós", "mundo", "python"]

# 4. Acceder a elementos
print(matriz_string[0][0]) # Imprime "adiós"
print(matriz_integer[1][2]) # Imprime 6