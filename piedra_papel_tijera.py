import random
import os

options = [
    "PIEDRA",
    'PAPEL',
    'TIJERA'
]

def run():

    puntos_maquina = 0
    puntos_jugador = 0
    while True:

        os.system("")
        os.system("cls")
        Maquina = random.choice(options).strip()
        Usuario = input(
            "Choice: \n1 -> PIEDRA \n2 -> PAPEL \n3 -> TIJERA \n: ").strip().upper()
        assert Usuario.isalpha(), "Tienes que escribir la palabra antes mencionada!"

        if Usuario == "PIEDRA" and Maquina == "TIJERA":
            puntos_jugador += 1
            print("GANA USUARIO\n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        elif Usuario == "TIJERA" and Maquina == "PAPEL":
            puntos_jugador += 1
            print("GANA USUARIO.\n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        elif Usuario == "PAPEL" and Maquina == "PIEDRA":
            puntos_jugador += 1
            print("GANA USUARIO!!\n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        elif Maquina == "PIEDRA" and Usuario == "TIJERA":
            puntos_maquina += 1
            print("PERDISTE !\n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        elif Maquina == "TIJERA" and Usuario == "PAPEL":
            puntos_maquina += 1
            print("PERDISTE !\n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        elif Maquina == "PAPEL" and Usuario == "PIEDRA":
            puntos_maquina += 1
            print("PERDISTE!\n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        else:
            print("EMPATE! \n")
            print(f"Elegiste {Usuario} y la pc eligio {Maquina}")

        print(f"JUGADOR: {puntos_jugador} \nMAQUINA: {puntos_maquina}")
        os.system("pause")
        os.system("cls")
        
        if puntos_jugador >= 3 or puntos_maquina >= 3:
            if puntos_maquina > puntos_jugador:
                print("Gano la maquina, la proxima sera!!")
            else:
                print("Has ganado tu, FELICITACIONES!")
            
            print("Termino el juego")
            break



if __name__ == '__main__':
    run()
