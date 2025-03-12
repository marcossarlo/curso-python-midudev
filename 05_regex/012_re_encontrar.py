import re

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias
print("\nEncontrar todas las coincidencias de un patrón:")
print("findall() devuelve una lista con todas las coincidencias:")
text = "Me gusta Pyshon. Python es lo máximo. Aunque Pydhon no es tan difícil, ojo con Pyxhon"
pattern = "Py.hon"
matches = re.findall(pattern, text)

print(matches)
print(f"La pabra Python se encontró {matches.count('Python')} veces")
# -------------------------

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda
print("\n.iter():\ndevuelve un iterador que contiene todos los resultados de la búsqueda:")
text = "Me gusta Pyshon. Python es lo máximo. Aunque Pydhon no es tan difícil, ojo con Pyxhon"
pattern = "Py.hon"
matches = re.finditer(pattern, text)
for match in matches:
  print(match.group(), match.start(), match.end())


# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"
print("\nEJERCICIO 02")
print("pattern:", pattern)
matches = re.finditer(pattern, text)
for match in matches:
  print(match.group(), match.start(), match.end())

print(f"Se encontró {len(re.findall(pattern, text))} veces")