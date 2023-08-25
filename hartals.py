import sys

def num_hartals(parties, days):
    days_with_hartals = set()
    for day in range(1, days + 1):
        for p in parties:
            if day == p or day % p == 0:
                days_with_hartals.add(day)
    return len(days_with_hartals)

sys.stdout.write("Ingrese la cantidad de casos: ")
T = int(sys.stdin.readline().strip())
cases = []

for _ in range(T):
    sys.stdout.write("Ingrese la cantidad de días del caso: ")
    N = int(sys.stdin.readline().strip())
    sys.stdout.write("Ahora ingresará los días por partido en una sola línea: ")
    number = sys.stdin.readline().strip()
    parties = list(map(int, number))
    cases.append(num_hartals(parties, N))

for i in cases:
    sys.stdout.write(f"{i}\n")
