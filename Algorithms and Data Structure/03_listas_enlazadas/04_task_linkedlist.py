"""
Ejercicio: Lista de Tareas con Lista Enlazada
Implementar una lista enlazada para gestionar una lista de tareas pendientes.
Requisitos: 
1. Definir una clase Nodo que almacene: 
    - La descripción de la tarea (str).
    - Un puntero al siguiente nodo.

2- Definir una clase llamada ListaTareas con los siguientes métodos:
    - agregar_tarea(descripcion): Agregar una nueva tarea al final de la lista.
    - mostrar_tareas(): Muestra todas las tareas en orden.
    - eliminar_tareas(descripcion): Busca y elimina una tarea por su descripción. 
    - buscar_tarea(descripcion): Devuelve True si la tarea existe en la lista, False si no.
    
3. Probar el código agregando varias tareas, mostrándolas, buscando una y eliminando otra.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def agregar_tarea(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def mostrar_tareas(self):
        if not self.head:
            print("No hay tareas registradas...")
            return
        
        temp = self.head
        while temp:
            print(f"Tarea: {temp.data}") 
            temp = temp.next

    def eliminar_tareas(self, string):
        temp = self.head
        
        if temp and temp.data == string:
            self.head = temp.next
            return True
        
        prev = None
        while temp and temp.data != string:
            prev = temp
            temp = temp.next
            
        if not temp:
            return False
        
        prev.next = temp.next
        return True

    def buscar_tarea(self, string):
        temp = self.head
        while temp:
            if temp.data == string:
                return True
            temp = temp.next
        return False

if __name__ == "__main__":
    task_list = TaskList()

    while True:
        print("\n___Gestionar Tareas___")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Buscar tarea")
        print("5. Salir")

        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opc == 1:
            try:
                n = int(input("Ingrese la cantidad de tareas que quiera registrar: "))
                for i in range(n):
                    string = input(f"Ingrese la tarea {i+1}: ")
                    task_list.agregar_tarea(string)
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opc == 2:
            task_list.mostrar_tareas()

        elif opc == 3:
            if task_list.head:
                tarea = input("Ingrese la tarea a eliminar: ")
                if task_list.eliminar_tareas(tarea):
                    print("La tarea se ha eliminado del registro.")
                else:
                    print("La tarea no fue encontrada.")
            else:
                print("No hay tareas registradas...")

        elif opc == 4:
            if task_list.head:
                tarea = input("Ingrese la tarea a buscar: ")
                if task_list.buscar_tarea(tarea):
                    print("La tarea se encuentra registrada.")
                else:
                    print("La tarea no se encuentra registrada.")
            else: 
                print("No hay tareas registradas...")

        elif opc == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")