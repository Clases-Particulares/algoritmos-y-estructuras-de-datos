# Lista: conjunto de datos de un mismo tipo

# ? En python las listas pueden contener datos de diferentes tipos
arreglo_int = [1, 2, 3, 4, 5]
arreglo_string = ["hola", "mundo", "python"]
arreglo_boolean = [True, False, True, False]
arreglo_mixto = [1, "hola", True]


# Operaciones con listas

# 1. Agregar elementos

arreglo_int.append(6)
arreglo_string.append("cuatro")
arreglo_boolean.append(True)

# 2. Eliminar elementos

arreglo_string.remove("mundo")
arreglo_int.remove(3)
arreglo_boolean.remove(False)

# 3. Modificar elementos

arreglo_boolean[0] = False
arreglo_int[0] = 0
arreglo_string[0] = "adios"

# 4. Acceder a elementos

print(arreglo_int[0])
print(arreglo_string[0])
print(arreglo_boolean[0])