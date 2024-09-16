# Crea diccionario con información de un perro
myDog={
    "name": "Firulais",
    "sex": "male",
    "age": 4,
    "fleas": [{"name":"bob"},{"name":"ignacio"},{"name":"smithers"}]

}

# Imprime el nombre
print(myDog["name"])

# Modifica el nombre y lo imprime
newName=input('Ingrese el nombre del perro:')
myDog["name"]=newName
print(myDog["name"])

# Crea nuevo elemento en el diccionario
myDog["color"]="black"
print(myDog)

print(myDog["fleas"][1]["name"])
print(myDog["fleas"])
