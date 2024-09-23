# Combinación de bloques try/except con with
try:
    archiveName=input('Ingrese el nombre del archivo:')
    file=open('data/'+archiveName)
except FileNotFoundError:
    print('El archivo no existe')
else:
    with file:
        # Lee todas las líneas del archivo
        # como una lista.
        lines=file.readlines()
        #print(lines)
        #for line in lines:
        #    print(line)
        for i in range(len(lines)):
            print(lines[i])