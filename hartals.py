import sys

def num_hartals(parties, days):
    days_with_hartals = set()
    for day in range(1, days + 1):
        for p in parties:
           if day % 7 != 6 and day % 7 != 0 and day % p == 0:
                days_with_hartals.add(day)
    return len(days_with_hartals)


T = int(sys.stdin.readline().strip())
cases = []

for _ in range(T):
    
    N = int(sys.stdin.readline().strip())
   
    number = sys.stdin.readline().strip()
    parties = list(map(int, number))
    print(parties)
    cases.append(num_hartals(parties, N))

for i in cases:
    sys.stdout.write(f"{i}\n")
