# Abre archivo junto con sentencia with.
# Asegura que se cierra el archivo
# una vez finalice el bloque with
with open(input('Ingrese el nombre del archivo:')) as file:
    question=file.readline()
    print(question)   



