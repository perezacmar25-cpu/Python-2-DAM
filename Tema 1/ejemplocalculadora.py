

seguir = "S"
while seguir.upper() != "N":
    print("Bienvenido a la calculadora Python")
    num1 = float(input("Di un número"))
    num2 = float(input("Di otro número"))
    print("Pulsa 1 si quiere sumar")
    print("Pulsa 2 si quiere restar")
    print("Pulsa 3 si quiere multiplicar")
    print("Pulsa 4 si quiere dividir")

    op = float(input())

    match (op):
        case 1:
            print(num1 + num2)

        case 2:
            print (num1-num2)

        case 3:
            print (num1*num2)

        case 4:
            while num2 == 0:
                print("No se puede dividir por 0")
                num2 = float(input ("Inténtalo de nuevo"))
            print(num1/num2)
        
        case _:
            print("Opción no válida")

    seguir = input("Quiere seguir S/N")