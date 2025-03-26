"""
Imagina que tienes una impresora que maneja varias tareas de impresión. Las tareas
se colocaran en una cola y se imprimen en el orden en que llegaron-
Escribe un programa que:
1. Agregue tareas de impresión (por ejemplo, "Documento 1", "Imagen 2") a la cola
2. Atienda la tarea de impresión de la cola en el orden que llegó.
3. Imprima las tareas a medida que se atienden y muestren un mensaje cuando todas 
las tareas se hayan completado.

Pistas:
- Usa una cola para agregar las tareas.
- Cada vez que se imprime una tarea, se elimina el primer elemento de la cola.
"""

from collections import deque


class Printer:
    
    def __init__(self):
        self.queue = deque()
        
    def add_task(self, task):
        self.queue.append(task)
        
    def print_task(self):
        if self.queue:
            print(f"Imprimiendo: {self.queue.popleft()}")
        else:
            print("Todas las tareas se han completado")
            
    def print_all_tasks(self):
        while self.queue:
            self.print_task()
        if not self.queue:
            print("Todas las tareas se han completado")
            
def taskOptions():
    task_options = ["Documento", "Imagen", "Texto"]    
    
    print(f"Tarea 1: {task_options[0]}")
    print(f"Tarea 2: {task_options[1]}")
    print(f"Tarea 3: {task_options[2]}")   
    
    opc = int(input("Elija una tarea: "))
    
    if opc == 1:
        return task_options[0]
    elif opc == 2:
        return task_options[1]
    elif opc == 3:
        return task_options[2]
    else:
        return None  


def menu():
    printer = Printer()
    

    while True:
        print("___IMPRESORA___")
        print("1. Agregar tarea")
        print("2. Imprimir tarea")
        print("3. Imprimir todas las tareas")
        print("4. Salir")
        print("________________")
        
        opc = int(input("Opción: "))
        if opc == 1:
            task = taskOptions()
            if task: 
                printer.add_task(task)
            else:
                print("Opción incorrecta")
            
        elif opc == 2:
            printer.print_task()
            
        elif opc == 3:
            printer.print_all_tasks()
            
        elif opc == 4:
            break
        
        else: 
            print("Opción incorrecta")
            
def main():
    menu()
    
if __name__ == "__main__":
    main()