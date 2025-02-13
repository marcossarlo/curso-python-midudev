import os
os.system("clear")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("Ejercicio 1: números del 10 al 1 usando un bucle while.")
number = 10
while number >= 1:
  print(number)
  number -= 1
else:
  print("Cuenta atrás completada")


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2: Suma de números pares (while)")
number = 1
even_number = 0
while number <= 20:
  if number % 2 == 0:
    print(number)
    even_number += number
  number += 1
else:
  print(f"La suma de los números pares entre 1 y 20 es: {even_number}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 a ese número. 
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3: Factorial de un número")
number = int(input("Introduce un número entero positivo: "))
number1 = number
factorial = 1
while number > 0:
  factorial *= number
  number -= 1
else:
    print(f"El factorial de {number1} es: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4: Validación de contraseña")
password = str(input("Introduce una contraseña (al menos 8 caracteres): "))
while len(password) < 8:
    password = str(input("Introduce una contraseña (al menos 8 caracteres): "))
else:
    print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5: Tabla de multiplicar")
number = int(input("Introduce un número: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6: Números primos hasta N") 
number = int(input("Introduce un número entero positivo: "))
i = 2
while i <= number:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        print(i)
    i += 1
else:
    print(f"Todos los números primos hasta {number} han sido impresos.")

