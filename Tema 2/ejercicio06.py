

palabras = ["hola","adios","mando"]

print("Lista original : ",palabras)

palabra1 = input("Di una palabra de la lista")
palabra2 = input("Por cuál quiere cambiarla")

for i in range (len(palabras)):

    if palabras[i] == palabra1:
        palabras[i] = palabra2


print(palabras)



