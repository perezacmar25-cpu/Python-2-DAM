limite = int(input("di un límite"))
total = 0
lista = ""

while total < limite:

    numeroParaSumar = int(input("di un número para sumar"))
    total+= numeroParaSumar
    lista = lista +"-"+ str(numeroParaSumar)

print(lista)