###
# EJERCICOS
###

import os
os.system("clear")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("Ejercicio 1: Determinar el mayor de dos números")
number_1 = int(input("Introduce el primer número: "))
number_2 = int(input("Introduce el segundo número: "))
if number_1 > number_2:
    print(f"{number_1} es mayor que {number_2}")
elif number_1 < number_2:
    print(f"{number_2} es mayor que {number_1}")
else:
    print("Son iguales")  

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\nEjercicio 2: Calculadora simple")
number_1 = float(input("Introduce un primer número: "))
number_2 = float(input("Introduce un segundo número: "))
operator = input("Introduce un operador matemático (+, -, *, /): ")
if operator == "+":
    result = number_1 + number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "*":
    result = number_1 * number_2
elif operator == "/":
    if number_2 == 0:
        result = "No se puede dividir entre cero"
    else:
        result = number_1 / number_2
else:
    result = "Operador no válido"

print(f"El resultado de la operación {number_1} {operator} {number_2} es {result}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nEjercicio 3: Año bisiesto")
year = int(input("Introduce un año: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} es un año bisiesto")
else:
    print(f"{year} no es un año bisiesto")
    
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("\nEjercicio 4: Categorizar edades")
age = int(input("Introduce una edad: "))
if age < 0:
    print("Edad no válida")
elif age >= 0 and age <= 2:
    print("Bebé")
elif age >= 3 and age <= 12:
    print("Niño")
elif age >= 13 and age <= 17:
    print("Adolescente")
elif age >= 18 and age <= 64:
    print("Adulto")
else:
    print("Adulto mayor")

