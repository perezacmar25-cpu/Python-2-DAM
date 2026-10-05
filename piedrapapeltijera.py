op1 = input("Elige una opción (piedra, papel o tijera): ")
op2 = input("Elige una opción (piedra, papel o tijera): ")

match (op1, op2):
    case (x, y) if x == y:
        print("Empate")
    case ("piedra", "papel") | ("papel", "tijera") | ("tijera", "piedra"):
        print("Gana jugador 2")
    case ("papel", "piedra") | ("piedra", "tijera") | ("tijera", "papel"):
        print("Gana jugador 1")
    case _:
        print("Opción no válida")