"""💥 2. Batalla de dados
Tú y la máquina lanzan un dado (número aleatorio entre 1 y 6).

El que saque el número más alto gana la ronda.

Juega 5 rondas y al final muestra el marcador (tú vs máquina) y quién ganó.

💡 Extra: Puedes usar input("Presiona Enter para lanzar...") para hacerlo más interactivo."""

import random as rd
import os
import time

class Camps:
    def __init__(self, player, machine, winner):
        self.player = player
        self.machine = machine 
        self.winner = winner 

class Game:
    def __init__(self):
        self.marcador = []
        

    def lanzar_dados(self, rounds):  
        for i in range(int(rounds)):
            input("\nPresione cualquier tecla para lanzar el dado: ")

            player = rd.randint(1,6)
            machine = rd.randint(1,6)
            if player == machine:
                print("Es un empate!:")
                winner = "Tie"
            elif player > machine:
                print("Has ganado la ronda!")
                winner = "Player Wins"
            else:
                print("Has perdido la ronda !")
                winner = "Machine Wins"
            print(f"Player: {player}\nMachine:{machine}")
            self.marcador.append(Camps(player, machine, winner))
            
    def mostrar_marcador(self):
        for i in range(1,4):
            print(i, end=", ")
            time.sleep(1)
          
        print("\n\tResultados de la ronda: ")
        for i, marcador in enumerate(self.marcador):
            print(f"\nRonda {i+1}\t{marcador.winner}")
            print(f"Player\t\tMachine\n{marcador.player}\t\t{marcador.machine}")
            
def menu():
    while True:
        gm: Game = Game()
        print("1. Jugar")
        print("2. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1":
                while True:
                    round = input("Introduzca las rondas para jugar: ")
                    if round.isdigit(): break
                    else: print("Número inválido...")
                gm.lanzar_dados(round)
                gm.mostrar_marcador()
                os.system("pause")
            case "2": break
            case _:print("Opcion invalida")            
        
def main():
    menu()
    
if __name__ == "__main__":
    main()
            