###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
# Se pueden modificar, agregar y eliminar elementos.
# se usan los corchetes [] para definir una lista.
# Se pueden acceder a los elementos de la lista por medio de su índice.
# Los índices en Python comienzan en 0.
###

import os
os.system("clear")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetín 1', 4]]
matrix = [[1, 2], [2, 3], [4, 'calcetín 2']]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice:")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])
print(matrix[2][1])

# Slicing (rebanado) de listas
print("\nSlicing de listas: \nlista[desde:hasta:pasos]")
list_slicing = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
print(list_slicing[2:4]) # ['tres', 'cuatro']
print(list_slicing[:3]) # ['uno', 'dos', 'tres']
print(list_slicing[3:]) # ['cuatro', 'cinco']
print(list_slicing[:]) # copia de la lista | ['uno', 'dos', 'tres', 'cuatro', 'cinco']

# HAY MÁS MAGIA
print("\nMás magia:")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[1::2]) # para devolver índices pares
print(lista1[::2]) # para devolver índices inpares
print(lista1[::-1]) # para devolver índices inversos

# Modificar una lista
print("\nModificar una lista:")
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
print("\nAñadir elementos a una lista:")
lista1 = [1, 2, 3]
print(lista1)

# forma larga y menos eficiente
print("Forma larga y menos eficiente")
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
print("Forma corta y más eficiente")
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("\nRecuperar longitud de una lista")
print("Longitud de la lista es:", len(lista1))

