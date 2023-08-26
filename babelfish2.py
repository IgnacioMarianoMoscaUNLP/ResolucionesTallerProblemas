
import sys
dictionary = {}

# Lectura del diccionario
while True:
    line = input().strip()
    if line == "":
        break
    english, foreign = line.split()
    dictionary[foreign] = english

# Traducción del mensaje
for line in sys.stdin:
    foreign_word = line.strip().lower()  # Convertir a minúsculas para manejar mayúsculas y minúsculas
    if foreign_word in dictionary:
        print(dictionary[foreign_word])
    else:
        print("eh")
