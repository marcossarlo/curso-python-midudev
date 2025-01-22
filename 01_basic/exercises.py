###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
### Completa aquí
name = "MArcosSarlo"
city = "Tarma - Perú"
print(f"Mi nombre es: {name}")
print(f"Mi ciudad es: {city}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
### Completa aquí
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
cadena = "12345"
print(int(cadena))
print(float(cadena))

print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")
float_number = 3.99
print(int(float_number))
### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
### Completa aquí
name = "MarccosSarlo"
age = 45
height = 1.68
print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
pi = 3.14159
rounded_pi = round(pi)
result = rounded_pi // 2
print(result)