shopping = ['agua','Huevos','Aceite','Sal','Limón']
products = ['agua','Huevos','Aceite','Sal','Limón','Pan','Leche','Cereal']

for product, detail in zip(products, shopping):
    print(f'Producto: {product}, Detalle: {detail}')

#Tuplas

# TUPLAS EN PYTHON
# Una tupla es como una lista, pero no se puede modificar (inmutable)

# Crear tuplas (con paréntesis)
vacia = ()
reyes = ("Melchor", "Gaspar", "Baltasar")
mezcla = ("a", 1, True)


# Tupla de un elemento: hay que poner coma
no_es_tupla = ("Papá Noel")    # esto es un str
si_es_tupla = ("Papá Noel",)   # esto es una tupla

# Sin paréntesis también vale
reyes2 = "Melchor", "Gaspar", "Baltasar"

# No se pueden modificar
# reyes[0] = "Tom Hanks"   # da TypeError

# Convertir a tupla
lista = ["Agua", "Aceite", "Arroz"]
tupla = tuple(lista)

# Operaciones permitidas
print(reyes[0])        # acceder por índice
print(len(reyes))      # longitud
print("Gaspar" in reyes)  # buscar un elemento

# NO se pueden usar: append, extend, remove, clear, sort, reverse

# Desempaquetado: guardar cada elemento en una variable
rey1, rey2, rey3 = reyes
print(rey1, rey2, rey3)

# Intercambiar valores
a = 40
b = 20
a, b = b, a
print(a, b)   # 20 40

# Desempaquetado con *
ranking = ("G", "A", "R", "Y", "W")
primero, *medio, ultimo = ranking
print(primero)   # G
print(medio)     # ['A', 'R', 'Y']
print(ultimo)    # W

# Tuplas vs listas (ventajas de las tuplas)
# 1. Ocupan menos memoria
# 2. Están protegidas contra cambios
# 3. Se pueden usar como claves de un diccionario
# 4. Las namedtuples son una alternativa sencilla a los objetos


#TypeError
t = (1,"hola",True)
ordenada = sorted(t)




