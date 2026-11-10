lista = [1,7,8,99,5,4]

op =int(input("Pulsa 1 si quiere buscar un elemento de la lista"))

match op :

    case 1:
        num =float(input("Di el número que quieras buscar"))

        if num in lista:
            indice = lista.index(num)
            print(f"Se encuentra en la posición {indice + 1}")    

        else:
            print("El número no está en la lista")

    case 2 :
        num = float(input("¿Qué número quiere insertar al final?"))
        lista.append(num)
        print(lista)

    case 3:
        num = int (input("¿En qué posición quiere?"))
        num1 = float(input("Di el número que quiera insertar"))

        lista.insert(num-1,num1)

        print(lista)

    case 4:
        num = input("¿Qué número quiere borrar")
        lista.remove(num)
        print(lista)

    case 5 :
        pos = int(input("¿Qué posición quiere borrar?"))
        del lista [pos - 1]
        print(lista)
