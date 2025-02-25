# La tienda "TecnoStore" vende productos electrónicos y cuenta con un registro de los precios de sus productos en un arreglo.
# El gerente desea conocer el precio promedio de los productos para evaluar estrategias de precios.
# Se dispone de un arreglo que contiene los precios (en dólares) de todos los productos disponibles en "TecnoStore".

# Desarrolla un programa que:
# * Recorra el arreglo para calcular el precio promedio.
# * Recuerda que el precio promedio se obtiene sumando todos los precios y dividiéndolos entre la cantidad total de productos.
# * Imprima el precio promedio obtenido.

articulos = []
precio_promedio = 0

cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
for i in range(cantidad_articulos):
    precio = float(input(f"Ingrese el precio del artículo {i + 1}: "))
    articulos.append(precio)

# calcular el precio promedio

for articulo in articulos:
    precio_promedio += articulo

precio_promedio = precio_promedio / cantidad_articulos

print(f"El precio promedio de los artículos es: {precio_promedio}")