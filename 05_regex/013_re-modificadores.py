### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

import re
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

print("Modificadores:")
print("re.IGNORECASE: Ignora las mayúsculas y minúsculas")
print("text:", text)
print("pattern:", pattern)

if found: print(found)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"
print("\nEJERCICIO 03")
print("pattern:", pattern)
print("text:", text)
found = re.findall(pattern, text, re.IGNORECASE)
if found: print(found)
print(f"Se encontró {len(found)} veces")
