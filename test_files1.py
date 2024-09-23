
# Abre archivo
file=open('data/my_data.txt','xt')

# Solicita texto al usuario
question=input('Ingrese su pregunta:')

# Escribe el texto en el archivo
file.write(question)

# Cierra el archivo
file.close()

