"""
Queremos desarrollar un pequeño programa que ayude a un técnico meteorológico (mi amigo Nico es
meteorólogo) a analizar las temperaturas registradas durante una semana en su estación de trabajo.
Rellenar la lista con temperaturas generadas de forma aleatoria entre dos límites leídos por teclado. Pueden
tener decimales.
A partir de esa lista, el programa debe:

Mostrar todas las temperaturas introducidas.
Calcular y mostrar la temperatura media.
Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron (día 1, día 2, no usar fechas).
Ordena la lista de mayor a menor temperatura.
Mostrar cuántos días tuvieron temperaturas por encima de la media.
Crear una nueva lista solo con las temperaturas superiores a la media.
"""

import random


seguir = 1
while seguir != 0:
    print("Bienvenido al programa")
    print("Pulsa 1 si quiere mostrar todas las temperaturas")
    print("Pulsa 2 si quiere calcular la media de las temperaturas")



    op = int(input())
    temperaturas = []
    temperaturas_encima_media = []
    temp_min = int(input("Di la temperatura mínima"))
    temp_max = int(input("Di la temperatura máxima"))

    for i in range(0,7):
                temperaturas.append(random.randint(temp_min,temp_max))

    match op:
        case 1:
            print(temperaturas)

        case 2:
            total_suma = 0

            for i in range (len(temperaturas)):
                total_suma += temperaturas[i]

            media = total_suma/len(temperaturas)
            print(media)

        case 4 :
            temp_ordenada = sorted(temperaturas,reverse=True)
            print(temp_ordenada)
            


        case 5 :
                cont = 0
                total_suma = 0
                for i in range (len(temperaturas)):
                    total_suma += temperaturas[i]
            
                media = total_suma/len(temperaturas)
                
                for i in range(len(temperaturas)):
                    if i > media:
                        cont+=cont

                print(f"{cont} días por encima de la media")


        case 6:
                total_suma = 0
                for i in range (len(temperaturas)):
                    total_suma += temperaturas[i]
                media = total_suma/len(temperaturas)
            
                for temperatura,temperatura_media in zip(temperaturas,temperaturas_encima_media):
                    if temperatura > media:
                        temperaturas_encima_media.append(temperatura)
                print(temperaturas_encima_media)

seguir = int(input("¿Desea seguir?"))
                    
        

        
