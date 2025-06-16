"""
Simulador del juego de piedra, papel y tijeras
"""
import random as rm
import os

jackes = {
    "Piedra" : "Tijera",
    "Tijeras" : "Papel",
    "Papel" : "Piedra"
}

def machine_elections() -> str:
    options = ["Piedra", "Papel", "Tijera"]
    return rm.choice(options)

def who_win(player, machine):
    print(f"\nSELECTIONS:\n\tPlayer: {player}\n\tMachine: {machine}")
    print("\nRESULTS:")
    if player == machine:
        return "\tIts Tie!\n"
    elif jackes[player] == machine:
        return "\tPlayer Wins!\n"
    else:
        return "\tMachine Wins!\n"

def play_menu():
    options = {
        1 : "Piedra",
        2 : "Papel",
        3 : "Tijeras"
    }

    while True:
        print("Elija: ")
        print("\t1- Piedra")
        print("\t2- Papel")
        print("\t3 - Tijeras")
        opc = int(input("Seleccione una opción"))
        if opc == 1 or opc == 2 or opc== 3:
            print(who_win(options[opc], machine_elections()))
            break
        else: print("Opcion invalida...")
    
def main_menu():
    while True:
        print("\n\n=== JUEGO PIEDRA, PAPEL O TIJERAS ===")
        print("1. Jugar")
        print("2. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1":
                play_menu()
                os.system("pause")
            case "2": 
                print("Saliendo...")
                break
            
            case _:print("Opción inválida")
            
def main():
    main_menu()
    
if __name__ == "__main__":
    main()