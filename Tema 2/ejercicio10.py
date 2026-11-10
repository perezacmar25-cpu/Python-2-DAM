palabras = ["hola", "adios", "mando", "perro", "gato", "gato", "mando"]

print(palabras)

sin_repetidos = []

for palabra in palabras:
    if palabra not in sin_repetidos:
        sin_repetidos.append(palabra)

print(sin_repetidos)