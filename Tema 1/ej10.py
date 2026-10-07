numeros=""

numero=input("introduce un número")

while numero != "":

    numeros = numeros + numero + "\n"
    numero = input("introduce un número")

print(numeros)