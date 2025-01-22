####################################################
# Tipado Dinámico:
# No necesitas declarar el tipo de dato explícitamente.
# Python deduce automáticamente el tipo de una variable en el momento en que le asignas un valor.
# se puede cambiar el tipo de una variable en tiempo de ejecución.
# Ventaja: Agilidad al escribir código.
# ⚠️ Desventaja: Puede haber errores si no controlas bien los tipos de datos.

####################################################
# Tipado Fuerte:
# No se permite operar entre tipos incompatibles sin conversión explícita.
# Por ejemplo, no puedes sumar directamente un número entero con una cadena.
# Si necesitas realizar operaciones entre tipos diferentes, debes convertir los valores explícitamente

# Tipado dinámico
x = 42          # Entero
print(type(x))  # <class 'int'>
x = "Hola"      # Ahora es un string
print(type(x))  # <class 'str'>

# Tipado fuerte
x = 42
y = "23"
# print(x + y)  # Esto genera un error.
print(x + int(y))  # Convertimos 'y' a entero: resultado 65.
