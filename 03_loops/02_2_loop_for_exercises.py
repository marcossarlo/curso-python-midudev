import os
os.system("clear")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1: Imprimir números pares")
number = 20
for i in range(2, number + 1, 2):
    print(i)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2: Calcular la media de una lista")
numbers = [10, 20, 30, 40, 50]
print("Números:", numbers)
sum = 0
for number in numbers:
    sum += number
average = sum / len(numbers)
print("Promedio:", average)


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3: Buscar el máximo de una lista")
numbers = [15, 5, 25, 10, 20]
print("Números:", numbers)
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print("Número máximo:", max)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4: Filtrar cadenas por longitud")
words = ["casa", "arbol", "sol", "elefante", "luna"]
print("Palabras:", words)
words_filtered = [word for word in words if len(word) >= 5]
print("Palabras con más de 5 letras:", words_filtered)


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5: Contar palabras que empiezan con una letra")
words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
print("Palabras:", words)
letter = input("Introduce una letra: ")
count = 0
for word in words:
    if word.lower().startswith(letter.lower()):
        count += 1
print(f"Número de palabras que empiezan con '{letter}': {count}")
