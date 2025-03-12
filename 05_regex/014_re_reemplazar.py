### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

import re

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"

print("Reemplazar el texto")
print(".sub() reemplaza todas las coincidencias de un patrón en un texto")
print("pattern:", pattern)
print("replacement:", replacement)


new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print("text:", text)
print("text replacement:", new_text)