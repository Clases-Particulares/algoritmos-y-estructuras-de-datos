# Encontrar el menor y mayor de una lista de numeros enteros
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Toma el primer numero del arreglo para tener una referencia
maximo = lista[0]
minimo = lista[0]

for i in lista:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i

# Muestra los resultados
print("El mayor es: ", maximo)
print("El menor es: ", minimo)