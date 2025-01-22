###
# 02 - types()
# Python tiene varios tipos de datos
# int, float, complex, str, bool, NoneType, list, tuple, dict, range, set...
###
print("Tipos de datos en Python:")
print("Int:")
# print(10)
# print(-10 + 5)
# print(4548785145454545653535)

print(10, type(10))
print(-10 + 5, type(-10 + 5))
print(45487851454545456535357878 + 1, type(4548785145454545653535))

print("\nFloat:")
print(10.0, type(10.0))
print(-10.0 + 5.3, type(-10.0 + 5.3))
print(1e3, type(1e3))

print("\nComplex:")
print(1 + 2j, type(1 + 2j))

print("\String:")
print("¡Hola, Twitch!", type("¡Hola, Twitch!"))
print("""
    Esto es multilinea
""")

print("\nBool:")
print(True, type(True))
print(False, type(False))
print(41 > 15, type(41 > 15))

print("\nNoneType:")
print(None, type(None)) # None es un tipo de dato especial que representa la ausencia de valor


