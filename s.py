from collections import Counter

# Leer la secuencia de enteros desde la entrada estándar
sequence = list(map(int, input().split()))

# Contar las ocurrencias de cada número utilizando Counter
counter = Counter(sequence)

# Imprimir los pares ordenados (número, ocurrencias) en el orden original
for number, count in counter.items():
    print(f"{number} {count}")
