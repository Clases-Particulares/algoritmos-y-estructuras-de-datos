# Ejercicio 4: Operaciones con Matrices y Vectores

## Objetivos:
# 1. Crear una matriz de tamaño 3x3 con valores enteros.
# 2. Crear un vector de tamaño 3 con valores enteros.
# 3. Realizar la multiplicación de la matriz por el vector.
# 4. Imprimir la matriz, el vector y el resultado de la multiplicación.

## Condiciones:
# - La matriz debe ser ingresada por el usuario.
# - El vector debe ser ingresado por el usuario.
# - Utilizar bucles para realizar la multiplicación.

# Crear una matriz de 3x3 con valores 0
# matriz = [[int(input(f"Ingresa el valor de la fila {i+1} y columna {j+1}: ")) for i in range(3)] for j in range(3)]
matriz = [
  [1, 4],
  [0, -1],
  [2, 5]
]

# vector = [int(input(f"Ingresa el valor del vector en la posición {i+1}: ")) for i in range(3)]
vector = [2, 3]

# Realizar la multiplicación de la matriz por el vector

vector_resultado = []

suma = 0
for i in range(3):
  suma = 0
  for j in range(2):
    suma += vector[j] * matriz[i][j]
  vector_resultado.append(suma)
print(vector_resultado)