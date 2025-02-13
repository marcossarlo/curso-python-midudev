# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# Función 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
def print_numbers(number: int):
    for i in range(1, number + 1):
        print(i)
print("Función 1: Imprimir números del 1 al número deseado")
print_numbers(5)

# Función 2: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
def multiplication_table(number: int):
    print("Tabla de multiplicar de", number)
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

print("\nFunción 2: Tabla de multiplicar")
number = int(input("Introduce un número: "))
multiplication_table(number)

# Función 3: Factorial de un número
def factorial_number(number: int):
    number1 = number
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1
    return f"El factorial de {number1} es: {factorial}"

print("\nFunción 3: Factorial de un número")
number = int(input("Introduce un número entero positivo: "))
print(factorial_number(number))

# Función 4: Números primos hasta N

def prime_numbers(number: int):
    for i in range(1, number + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)

print("\nFunción 4: Números primos hasta N")
number = int(input("Introduce un número entero positivo: "))
prime_numbers(number)
