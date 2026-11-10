
texto = input("Di una palabra o frase ").lower()


letras_vistas = []
es_isograma = True

for caracter in texto:

    if caracter.isalpha():
        if caracter in letras_vistas:
            es_isograma = False
            break
        letras_vistas.append(caracter)


if es_isograma:
    print(f"'{texto}' es un isograma")
else:
    print(f"'{texto}' no es un isograma")