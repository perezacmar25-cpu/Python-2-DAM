palabras = []
num =  int(input("Cuántas palabras quiere meter"))

for i in range (num) :
    palabra = input("Diga una palabra para introducir")
    palabras.append(palabra)

palabra_borrar = input("Di una para borrar")

for i in range (len(palabras)):
    if palabra_borrar == palabras[i]:
        palabras.remove(palabra_borrar)

print(palabras)