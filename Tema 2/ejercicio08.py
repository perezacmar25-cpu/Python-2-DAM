palabras = ["hola", "adios", "mando"]

palabras2 = ["perro", "gato", "mando"]

print(palabras)
print(palabras2)
for palabra in palabras2:
    if palabra in palabras:
        palabras.remove(palabra)


print(palabras)
print(palabras2)