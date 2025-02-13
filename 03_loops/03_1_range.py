import os
os.system("clear")

###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("\nrange():")

# Generado una secuencia de números del 0 al 9
print("Generando una secuencia de números del 0 al 9")
for num in range(10):
  print(num) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(inicio, fin)
print("Generando una secuencia de números del 5 al 9")
for num in range(5, 10):
  print(num) # 5, 6, 7, 8, 9

# range(inicio, fin, paso)
print("Generando una secuencia de números del 0 al 9, de dos en dos")
print("range(inicio, fin, paso)")
for num in range(0, 10, 2):
  print(num) # 0, 2, 4, 6, 8

print("Generando una secuencia de números del -5 al 0")
for num in range(-5, 0):
  print(num) # -5, -4, -3, -2, -1

print("Rango descendente")
for num in range(10, 0, -1):
  print(num) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

print("Convirtiendo un rango en una lista")
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# seria para hacerlo cinco veces
print("\nhacer cinco veces algo")
for _ in range(5):
  print("hacer cinco veces algo")