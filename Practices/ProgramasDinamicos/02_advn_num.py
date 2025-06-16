"""
🎯 1. Adivina el número
        La máquina elige un número aleatorio del 1 al 100.

        Tú intentas adivinarlo.

        El programa te dice si estás "muy alto" o "muy bajo".

        Cuando aciertas, muestra cuántos intentos te tomó.

💡 Extra: Guarda el récord de menor cantidad de intentos (en una variable).
"""

import datetime as dt
import random as rm
import os

class Historial:
    def __init__(self, intentos: int, fecha: dt):
        self.intentos = intentos
        self.fecha = fecha

class RandomMachine:
    def __init__(self):
        self.historial = []
        
    def elegir_num(self):
        random_num = rm.randint(1, 100)
        intentos = 0
        num = int(input("Seleccione un numero entre el 1 al 100: "))
        while True:
            if num == random_num:
                print(f"\nHas acertado, el número elegido por la maquina es: {random_num}")
                print(f"Numeros de Intentos: {intentos}")
                self.historial.append(Historial(intentos, dt.datetime.now()))
                break
            if num > random_num:
                print("\nTe has pasado!!!")
                intentos += 1
                os.system("pause")
            if num < random_num:
                print("Estas abajo!!!")
                intentos += 1
                os.system("pause")
                
    def mostrar_historial(self):
        for i in self.historial:
            print(f"{i+1}. {self.historial[i].fecha}\n\tIntentos: {self.historial[i].intentos}")
            
    def mostrar_record(self):
        return min(self.historial.intentos)
    
def menu():
    adv: RandomMachine = RandomMachine()
    while True:
        print("==== ADIVINA EL NÚMERO ====")
        print("1. Elegir Numero")
        print("2. Mostrar Historial de Intentos")
        print("3. Mostrar Recórd")
        opc = input("Elija una opción: ")
        match opc:
            case "1":
                adv.elegir_num()
            case "2":
                adv.mostrar_historial()
            case "3":
                adv.mostrar_record()
            case _:
                print("Opcion invalida...")
                
def main():
    menu()
    
if __name__ == "__main__":
    main()