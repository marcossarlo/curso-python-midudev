import os
os.system("clear")

###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

print("\nBucle for:")

# Iterar una lista
print("Iterar una lista:")
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier cosa que sea iterable
print("\nIterar sobre cualquier cosa que sea iterable:")
cadena = "midudev"
for caracter in cadena:
  print(caracter)

# enumerate()
print("\nenumerate():")
frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
  print(f"El índice está {idx} y la fruta es {value}")

# bucles anidados
print("\nBucles anidados:")
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")

# break
print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
print("Lista: ", animales)
for idx, animal in enumerate(animales):
  print(animal)
  if animal == "loro":
    print(f"El loro está escondido en el índice {idx}")
    break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro": 
    continue  
  
  print(animal)


# Comprensión de listas (list comprehension):
# Es una forma de crear listas de forma más rápida y sencilla, en una sola línea de código
print("\nComprensión de listas:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
print(animales)
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
print("\nMuestra los números pares de una lista:")
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]
print(pares)