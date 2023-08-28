import sys

N,M = sys.stdin.readline().split()

while int(N)!=0 and int(M)!=0:
    disks = []
    pairs = 0
    for i in range(int(N)+int(M)):
        d = int(sys.stdin.readline())
        if(d in disks):
           pairs+=1 
        else:
            disks.append(d)   
    sys.stdout.write(str(f"{pairs}\n"))
    N,M = sys.stdin.readline().strip().split()