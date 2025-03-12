##
# 01 - Expresiones Regulares (Regex)
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1. Importar el módulo de expresiones regulares "re"
import re
# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
print("pattern:", pattern)
# 3. El texto donde queremos buscar
text = "Hola mundo"
print("text:", text)
# 4. Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if result:
  print("He encontrado el patrón en el texto")
else:
  print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el pattern
print("\n.group() devuelve la cadena que coincide con el pattern")
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(".start() devuelve la posición inicial de la coincidencia")
print(result.start())

print(".end() devuelve la posición final de la coincidencia")
# .end() devolver la posición final de la coincidencia
print(result.end())


# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
print("\nEJERCICIO 01")
print("pattern:", pattern)
print("text:", text)

found_ia = re.search(pattern, text)

if found_ia:
  print(f"-> He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
  print("No he encontrado el patrón en el texto")