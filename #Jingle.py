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

while True:
    melody = sys.stdin.readline().strip()
    if(melody=="*"):
        break
    melody= melody[1:-1]    
    melody = melody.split("/")
    total=0
    for measure in melody:
        value=0
        for x in measure:
            value+= notes[x]
        if value ==1:
            total+=1       
    print(total)        