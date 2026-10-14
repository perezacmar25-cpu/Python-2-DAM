
saldo = 1000.0
seguir = "S"
while seguir.upper()!= "N":
    print("Bienvenido al cajero automático")

    
    print("Pulsa 1 si quiere ver su saldo")
    print("Pulsa 2 si quiere retirar dinero")
    print("Pulsa 3 si quiere ingresar dinero")
    print("Pulsa 4 si quiere comprar entradas")
    op= int(input())

    match op : 

        case 1 :
            print(saldo)

        case 2 :
            
            retirada = float(input("¿Cuánto quiere retirar?"))

            if retirada > saldo:
                print("Error")
            else:
                saldo = saldo - retirada


        case 3:

            
            ingreso = float(input("¿Cuánto quiere ingresar?"))
            if ingreso < 0:
                print("Error")

            else:
                saldo = saldo + ingreso


        case 4 :
            numero = float(input("¿Cuántas quiere comprar?"))
            if numero < 0:
                print("Error")

            else :
                precio = float(input("¿Cuánto vale cada una?"))

            if precio < 0:
                print("Error")

            else:
                total = numero * precio

            if total > saldo:
                print("Saldo insuficiente")

            else :
                saldo-=total


        case _ :
            print("Opción no válida")


    seguir = input ("¿Desea seguir? S/N")


