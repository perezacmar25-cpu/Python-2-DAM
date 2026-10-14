import random
numero_secreto = random.randint(0,10)
numero_intentos = 0

while numero_intentos < 3 :

    numero = int(input("Di un número"))
    numero_intentos+=1
    if numero == numero_secreto:
        print("Has acertado")
        break

    else:
        print("Has fallado")


if numero != numero_secreto:
    print(numero_secreto)