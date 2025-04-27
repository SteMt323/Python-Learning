"""
Lista de tareas con prioridad
- Inserta tareas con prioridad (por número).
- Inserta de forma ordenada.
- Eliminar la tarea con menor prioridad.
- Buscar tareas específicas.
"""
import os

class Task:
    def __init__(self, task: str, priority: int):
        self.task = task 
        self.priority = priority
        
class Node:
    def __init__(self, data: Task):
        self.data = data
        self.next = None
        self.prev = None
        
class TaskList:
    def __init__(self):
        self.head = None
        
    def append(self, task, priority):
        new_node: Node = Node(Task(task, priority))
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def print_sorted(self):
        if not self.head:
            print("Sin listas registradas...")
            return
        task = []
        current = self.head
        while current:
            task.append(current.data)
            current = current.next
            
        task.sort(key=lambda x: x.priority, reverse=True)
        
        for index, task in enumerate(task, start=1):
            print(f"{index}. {task.task}\tPrioridad: {task.priority}") 
            
                
    def delete_minor_priority(self):
        if not self.head:
            print("Sin tareas registradas...")
            return
        
        for priority in range(1, 6):
            current = self.head
            while current:
                prev_node = current.prev
                next_node = current.next
                if current.data.priority == priority:
                    # Evaluar el head
                    if self.head.data.priority == priority:
                        self.head = next_node
                        if self.head:
                            self.head.prev = None
                        return

                    # Evaluar el tail
                    if not current.next:
                        prev_node.next = None
                        return
                    # Evaluar demas casos
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    return
                
                current = current.next
                
    def search_task(self, task) -> str:
        if not self.head:
            print("Sin tareas registradas...")
            return
        
        current = self.head
        while current:
            if current.data.task == task:
                return f"Tarea: {current.data.task}\tPrioridad: {current.data.priority}"
            
            current = current.next
        print("Tarea no encontrrada...")
            
        
            
            
        
            
def menu():
    task_list: TaskList = TaskList()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("LISTA DE TAREAS")
        print("1. Agregar Tareas")
        print("2. Mostrar Tareas")
        print("3. Buscar Tareas")
        print("4. Eliminar Tareas")
        print("5. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                nombre = input("Ingrese el nombre de la tarea: ")
                while True:
                    prioridad = int(input("Ingrese la prioridad de la tarea (1 - 5): "))
                    if prioridad not in range(1,6):
                        print("ERROR: Debe de introducir un entero (1 - 5)....")
                    else: 
                        task_list.append(nombre, prioridad)
                        break
                    
            case "2":
                task_list.print_sorted()
                os.system("pause")
                
            case "3":
                task = input("Introduzca la palabra a buscar: ")
                print(task_list.search_task(task))
                os.system("pause")
                
            case "4":
                task_list.delete_minor_priority()
                os.system("pause")

            case "5":
                print("Saliedo...")
                break
            
            case _:
                print("Opción inválida, intente nuevamente...")
                os.system("pause")                
                
                
def main():
    menu()
    
if __name__ == "__main__":
    main()
        