num_notas = int(input("Cuántas notas tienes"))
lista  = []
suma_notas = 0

while len(lista) < num_notas:
    nota = float(input("Di la nota"))
    
    if nota >= 0:  
        lista.append(nota)
    else:
        print("La nota debe ser mayor o igual que 0")

print(lista)

for i in range(len(lista)):
    suma_notas =suma_notas + lista[i]

nota_media = suma_notas/2

print(f"Nota media : {nota_media}")

nota_mas_alta = 0
for i in range (len(lista)):
    
    if lista[i] > nota_mas_alta :
        nota_mas_alta = lista[i]


print (nota_mas_alta)