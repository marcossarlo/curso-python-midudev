###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

print("Conversión (Casting) de tipos en Python:")
#print("100" + 2) # TypeError: can only concatenate str (not "int") to str
print("Cast de enteros:")
print(int("100") + 2)
print("100" + str(2))

print("Cast de flotantes:")
print(float("100.5"))
print(float(100))

print("Cast de booleanos:")
print(bool(1))
print(bool(0))
print(bool(-1))

print(bool("Hola"))
print(bool(""))
print(bool(" "))
print(bool("False"))