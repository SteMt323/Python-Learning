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
        while True:
            num = int(input("Seleccione un numero entre el 1 al 100: "))
            if num == random_num:
                print(f"\nHas acertado, el número elegido por la maquina es: {random_num}")
                print(f"Numeros de Intentos: {intentos}")
                self.historial.append(Historial(intentos, dt.date.today()))
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
        for i, historial in enumerate(self.historial):
            print(f"{i+1}. Intentos: {historial.intentos} - Fecha: {historial.fecha}")
            
    def mostrar_record(self):
        historial = self.historial
        record = None
        for i, intentos in enumerate(historial):
            if not record: record = intentos.intentos
            if intentos.intentos < record:
                record = intentos.intentos
                
        return record
    
def menu():
    adv: RandomMachine = RandomMachine()
    while True:
        print("\n\n==== ADIVINA EL NÚMERO ====")
        print("1. Elegir Numero")
        print("2. Mostrar Historial de Intentos")
        print("3. Mostrar Recórd")
        print("4. Salir")
        opc = input("Elija una opción: ")
        match opc:
            case "1":
                adv.elegir_num()
            case "2":
                adv.mostrar_historial()
            case "3":
                print(adv.mostrar_record())
            case "4":
                break
            case _:
                print("Opcion invalida...")
                
def main():
    menu()
    
if __name__ == "__main__":
    main()