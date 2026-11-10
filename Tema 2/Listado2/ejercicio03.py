import random


diccionario = {"66578905E":random.randint(0,10),"77443234T":random.randint(0,10)}

print("Pulsa 1 si quiere mostrar los datos")

op = int(input())

match op:
    case 1:
        print(diccionario)

    case 2:
        modificar_nota = float(input("Introduce la nota"))
        diccionario["66578905E"] = modificar_nota

    case 3:
        dni = input("Indica el DNI")
        diccionario[dni] = random.randint(0,10)


    case 4:
        diccionario_2 = {}
        valor = float(input("Di un valor: "))
        suma_notas = 0

        for dni, nota in diccionario.items():
            suma_notas += nota
            if nota > valor:
                diccionario_2[dni] = nota

        print(diccionario_2)




