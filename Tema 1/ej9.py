texto = ""
palabra = input("introduce una palabra")

while palabra != "":
    texto = texto + palabra + "\n"
    palabra = input("introduce una palabra")
print(texto)