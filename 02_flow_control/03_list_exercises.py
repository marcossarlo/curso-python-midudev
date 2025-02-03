###
# EJERCICOS
###
import os
os.system("clear")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("\nEjercicio 1: El mensaje secreto")
message = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
#only_secret = message[7:14]
only_secret = message[7:]
print(message)
print(only_secret)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2: Intercambio de posiciones")
numbers = [10, 20, 30, 40, 50]
print(numbers)
first_position = numbers[0]
last_position = numbers[-1]
numbers[0] = last_position
numbers[-1] = first_position
print(numbers)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("\nEjercicio 3: El sándwich de listas")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nEjercicio 4: Duplicando la lista")
list = [1, 2, 3]
print(list)
#new_list = list + list
list += list
print(list)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\nEjercicio 5: Extrayendo el centro")
list = [10, 20, 30, 40, 50, 60, 70]
print(list)
center = list[len(list)//2]
print(center)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\nEjercicio 6: Reversa parcial")
list = [1, 2, 3, 4, 5, 6]
print(list)
half = len(list)//2
first_half = list[:half]
second_half = list[half:]
first_half.reverse()
list = first_half + second_half
print(list)