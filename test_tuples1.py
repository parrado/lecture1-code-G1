# Crea tupla con 3 nombres de fruta
thisTuple = ("apple", "banana", "cherry")
thisTuple2=("carro",3.141592654,[1,2,3,4])

# Imprime el primer elemento de la tupla
print(thisTuple[0])

# Recorre la tupla con ciclo for
# e imprime cada uno de los elementos
for item in thisTuple:
    print(item)

for i in range(len(thisTuple)):
    print(thisTuple[i])


thisTuple[2]='Strawberry'