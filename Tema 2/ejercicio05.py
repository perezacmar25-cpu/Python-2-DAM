lista = []
cont = 0

num = int(input("Diga el tamaño de la lista"))

if num<0 :
    print("El tamaño debe ser mayor que 0")

else:
    for i in range (num):
        palabra = input("Diga una palabra")
        lista.append(palabra)

    palabraComparar = input("Di una palabra de la lista")

    for i in range (len(lista)):
        if lista[i] == palabraComparar:
            cont += 1

    print(f"La palabra aparece {cont} veces en la lista")

    