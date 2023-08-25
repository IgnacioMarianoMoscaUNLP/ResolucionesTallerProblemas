#jolly jumper
import sys
def is_jolly(sequence):
    n = sequence[0]
    differences = set()

    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i+1])
        differences.add(diff)

    # Comprobamos si las diferencias son exactamente los valores 1 hasta n-1
    for diff in range(1, n):
        if diff not in differences:
            return False
    return True

for line in sys.stdin:
    sequence = list(map(int,line.split()))
    if(is_jolly(sequence)):
        sys.stdout.write("Jolly\n")
    else:
        sys.stdout.write("Not jolly\n")  
                         