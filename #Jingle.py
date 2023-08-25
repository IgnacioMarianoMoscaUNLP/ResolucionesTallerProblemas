#Jingle
import sys
notes = {
    "W":1,
    "H":1/2,
    "Q":1/4,
    "E":1/8,
    "S":1/16,
    "T":1/32,
    "X":1/64
    
}

def is_one(m):
    value=0
    for x in m:
        value+= notes[x]
    return value==1            


while True:
    melody = sys.stdin.readline().strip()
    if(melody=="*"):
        break
    melody= melody[1:-1]    
    melody = melody.split("/")
    total=0
    for measure in melody:
        if(is_one(measure)):
            total+=1       
    sys.stdout.write("{:}".format(total))        