# Dado un vector de números reales, realiza lo siguiente:

# 1. Calcula la suma de todos sus elementos.
# 2. Calcula el promedio de dichos elementos.
# 3. Muestra en pantalla los elementos que son mayores que el promedio obtenido.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# calcula la suma

suma = 0
for i in lista:
  suma += lista[i]

print("La suma de todos los elementos es: ", suma)

# calcula el promedio de los elementos

promedio = 0
for i in lista:
  promedio += lista[i]

promedio = promedio / len(lista)

print("El promedio de todos los elementos es: ", promedio)

# muesta los elementos mayores al promedio

valores_mayores_al_promedio = []
for i in lista:
  if lista[i] > promedio:
    valores_mayores_al_promedio.append(lista[i])

print("Los valores mayores al promedio obtenido son: ", valores_mayores_al_promedio)