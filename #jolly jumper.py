import sys

def num_hartals(parties,days):
    i=0
    days_with_hartals = set()
    for day in range(1,days+1):
        for p in parties:
            if((day == p)or(day %p==0)):
                days_with_hartals.add(day)     
    return len(days_with_hartals)

sys.stdout.write("ingrese la cantidad de casos")
T = int(sys.stdin.readline().strip())
cases = []
for x in range(T):
    sys.stdout.write("ingrese la cantidad de dias del caso")
    N = int(sys.stdin.readline().strip())
    sys.stdout.write("ahora ingresara los dias por patido en una sola linea")
    number = sys.stdin.readline().strip()
    parties = [int(digit) for digit in number]
    cases.append(num_hartals(parties,N))

for i in cases:
    sys.stdout.write(f"{i}\n")        