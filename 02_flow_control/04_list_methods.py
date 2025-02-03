###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

import os
os.system("clear")

lista1 = ['a', 'b', 'c', 'd']
print(lista1)

# Añadir o insertar elementos a la lista

print("\nAñade un elemento al final:")
lista1.append('e') # Añade un elemento al final
print(lista1)

print("Inserta un elemento en la posición que le indiquemos como primer argumento:")
lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

print("Agrega elementos al final de la lista:")
lista1.extend(['😃', '😍']) # 
print(lista1)

# Eliminar elementos de la lista
print("remove(): Eliminar con remove:")
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

print("pop(): Eliminar el último elemento de la lista y además te lo devuelve")
ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print("Elemento a eliminar:", ultimo)
print(lista1)
print("Eliminar el segundo elemento de la lista (es el índice 1):")
lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia
print("Eliminar por lo bestia con del:")
del lista1[-1]
print(lista1)

print("clear(): Eliminar todos los elementos de la lista:")
lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
print("del(): Eliminar un rango de elementos con del:")
lista_animales = ['🐼', '🐨', '🐶', '😿', '🐹']
print(lista_animales)
del lista_animales[1:3]
print(lista_animales)

# Más métodos útiles
print("\nMás métodos útiles:")
numbers = [3, 10, 2, 8, 99, 101]
print(numbers)
print('Ordenar listas modificando la original')
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
print("\nCositas útilies:")
animals = ['🐶', '🐼', '🐨', '🐶']
print(animals)
print("Tamaño de la lista animals:", len(animals)) # Tamaño de la listas -> 4
print("Cuantas veces aparece el elemento 🐶:", animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print("Comprueba si hay un 🐼 en la lista:", '🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print("Comprueba si hay un 🐹 en la lista:", '🐹' in animals) # -> False