palabras = ["hola", "adios", "mando", "perro", "gato", "rana"]
palabras2 = ["persona","animal", "mando","gato", "perro","raton"]

palabras_en_las2 = []

for palabra in palabras2:
    if palabra in palabras:
        palabras_en_las2.append(palabra)


print("Palabras en las 2 ",palabras_en_las2)


palabras_en_la_1 = []

for palabra in palabras :
    if palabra not in palabras2:
        palabras_en_la_1.append(palabra)

print(palabras_en_la_1)


palabras_en_la_2 = []
for palabra in palabras2 :
    if palabra not in palabras:
        palabras_en_la_2.append(palabra)

print(palabras_en_la_2)

    


palabras_en_ambas = []
for palabra in palabras :

    if palabra in palabras2:
        palabras_en_ambas.append(palabra)

print(palabras_en_ambas)

