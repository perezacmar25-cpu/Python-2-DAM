"""
En una empresa de transporte se quiere guardar el nombre de los conductores que tiene y los kilómetros
que conducen cada día de la semana. Para guardar esta información se van a utilizar dos listas:
• Nombre: Lista para guardar los nombres de los conductores.
• kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza cada conductor.
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

"""

conductores = ["Mario","Raúl","Álvaro"]
km = {}

for conductor in conductores:
   lista_conductor = []
   print(f"Conductor: {conductor}")
   for dia in range(1,8):
      kilometro = float(input(f"Di los kilómetros del día {dia}"))
      lista_conductor.append(kilometro)
      km[conductor] = lista_conductor

print(km)
for conductor in conductores:
    lista_actual = km[conductor]

    suma = sum(lista_actual)

    print(f"Suma total de {conductor} es {suma}")













