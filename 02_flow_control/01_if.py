###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###
import os
os.system("clear")

print("\nSentencia simple condicional:")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

print("\nSentencia condicional con else:")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\nSentencia condicional con elif:")
nota = 7.5

if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")


print("\nCondiciones múltiples:")
edad = 17
tiene_licencia = True

# JavaScript -> Python
## && -> and
## || -> or

# 🇻🇪 un pueblo de Valencia
if edad >= 18 and tiene_licencia:
  print("Puedes conducir 🚗")
else:
  print("No puedes conducir, POLICIA 🚔!!!1!!!")

# 🇻🇪 un pueblo de Isla Margarita
if edad >= 18 or tiene_licencia:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

print("\nNot:")
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")

print("\nAnidar condicionales:")
edad = 20
tiene_dinero = True

#Más complicado: evitar muchas anidaciones
if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

#Más fácil:
if edad < 18:
  print("No puedes entrar a la disco")
elif tiene_dinero:
  print("Puedes ir a la discoteca")
else:
  print("Quédate en casa")

print("\n")
numero = 5
if numero: # True
  print(f"{numero}: El número no es cero")

numero = 0
if numero: # False
  print("Aquí no entrará nunca")

nombre = "Juan"
if nombre:
  print(f"{nombre}: El nombre no es vacío")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación
print(es_el_tres)
if es_el_tres:
  print("El número es 3")

print("\nLa condición ternaria:")
# La condición ternaria en Python es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 23
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(edad, mensaje)

#Más ejemplos de la condición ternaria:
numero = 8
es_par = "Es par" if numero % 2 == 0 else "Es impar"
print(numero, es_par)

# Otra forma de hacerlo:
es_par = "Es par" if not numero % 2 else "Es impar"
print(numero, es_par)

