#Babelfish
# Abre el archivo en modo lectura
import sys
    
dictionary={}
i=0
    
while True:
    line = input().strip()
    if line == "":
        break
    english, foreign = line.split()
    dictionary[foreign] = english
    
while True:
    line = input().strip()
    if line == "":
        break
    foreign = line.strip()        
    if(foreign in dictionary):
        sys.stdout.write(str(dictionary[foreign]+"\n"))
    else:
        sys.stdout.write("eh\n") 
    i+=1
           