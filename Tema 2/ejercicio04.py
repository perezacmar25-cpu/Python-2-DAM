lista = []
num = int(input("Di un número"))

if num < 0:
    print("El número tiene que ser positivo")
else:
    for _ in range (num):
        palabra = input("Diga una palabra")
        lista.append(palabra)



print(lista)