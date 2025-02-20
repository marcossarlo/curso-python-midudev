###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

print(persona)
# para acceder a los valores
print("Acceder a los valores:")
print(persona["nombre"]) # midudev
print(persona["edad"]) # 25
print(persona["calificaciones"][2])  # 9
print(persona["socials"]["twitter"]) # @midudev

# cambiar valores al acceder
persona["nombre"] = "madeval"
persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
print("\nEliminar completamente una propiedad")
del persona["edad"]
print(persona) # edad ya no existe

print("\nUso de pop(): recupera el valor, y lo elimina")
es_estudiante = persona.pop("es_estudiante") 
print(persona) # es_estudiante ya no existe
print(f"es_estudiante: {es_estudiante}") # True

# update(): sobreescribir un diccionario con otro diccionario
print("\nUpdate(): Sobreescribir un diccionario con otro diccionario:")
a = { "name": "miduev", "age": 25 }
print("a", a)
b = { "name": "madeval", "es_estudiante": True }
print("b", b)

a.update(b)
print("a", a)

# comprobar si existe una propiedad
print("\nComprobar si existe una propiedad:")
print("name" in persona) # False
print("nombre" in persona) # True

# obtener todas las claves
print("\nObtener todas las keys:")
print("Diccionario persona:", persona)
print(persona.keys()) # dict_keys(['nombre', 'calificaciones', 'socials'])

# obtener todas los valores
print("\nObtener todas las values:")
print(persona.values()) # dict_values(['madeval', [7, 8, 10], {'twitter': '@midudev', 'instagram': '@midudev', 'facebook': 'midudev'}])

# obtener tanto clave como valor
print("\nitems: obtener tanto clave como valor, en forma de Tuplas")
print(persona.items()) # dict_items([('nombre', 'madeval'), ('calificaciones', [7, 8, 10]), ('socials', {'twitter': '@midudev', 'instagram': '@midudev', 'facebook': 'midudev'})])

print("\nFor")
# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}
for key, value in persona.items():
  print(f"{key}: {value}")