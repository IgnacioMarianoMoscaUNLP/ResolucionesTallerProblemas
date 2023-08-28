
import sys
line = sys.stdin.readline().strip().split()
set_of_line = []
for i in line:
    if not i in set_of_line:
        sys.stdout.write(str(f"{i} {line.count(i)}\n"))
    set_of_line.append(i)