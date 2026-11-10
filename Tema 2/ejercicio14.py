
palabra = input("Di una palabra")

palabra_minuscula = palabra.lower()


if palabra_minuscula == palabra_minuscula[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo")
else:
    print(f"La palabra '{palabra}' no es un palíndromo")