
import sys
with open("archivo.txt", "r") as archivo:
    # Realizar operaciones en el archivo
    line = archivo.read()
    # No es necesario cerrar el archivo aquí, ya que el bloque 'with' lo hará automáticamente al salir
    set_of_line = []
    for i in line:
        if not i in set_of_line:
            sys.stdout.write(str(f"{i} {line.count(i)}\n"))
        set_of_line.append(i)