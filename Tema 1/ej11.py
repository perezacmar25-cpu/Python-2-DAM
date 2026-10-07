limite = int(input("Di un límite"))
total = 0
lista = ""

while total < limite:

    numeroParaSumar = int(input("Di un número para sumar"))
    total+= numeroParaSumar
    lista = lista +"-"+ str(numeroParaSumar)

print(lista)