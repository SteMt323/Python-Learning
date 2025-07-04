"""
🧠 3. Simón dice (nivel 1)
La máquina muestra una secuencia de colores (ej: ["rojo", "verde", "azul"]) que va creciendo cada ronda.

Tú debes repetirla en orden.

Si fallas, se termina el juego y te dice cuántas rondas superaste.

💡 Empieza con una lista vacía y cada ronda agrega un color aleatorio de ["rojo", "verde", "azul", "amarillo"].
"""
import random as rd
import time
import os 

class SimonSays:
    def __init__(self):
        self.colors = ["rojo", "verde", "azul", "amarillo"]
        self.simon_list = []
        
    def start_game(self):
        player_match = True
        while player_match:
            self.simon_list.append(rd.choice(self.colors))
            print("\nSimons Says: ")
            for simon in self.simon_list:
                print(simon)
                
            for i in range(1,4):
                print(i, end=", ")
                time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')   
            print("Rewrite the colors...")
            
            for i in range(len(self.simon_list)):
                color = input(f"Write the color {i+1}: ") 
                if color != self.simon_list[i]:
                    player_match = False
                    break
                
        print("Has perdido...")
        
        
def menu():
    simon_says: SimonSays= SimonSays()
    while True:
        print("1. Play")
        print("2. Exit")
        opc = input("Choce one option: ")
        match opc:
            case "1": simon_says.start_game()
            case "2": break
            case _: print("Invalid input...")
            
def main():
    menu()
if __name__ == "__main__":
    main()