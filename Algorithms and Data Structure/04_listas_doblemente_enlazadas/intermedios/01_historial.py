"""
Simular un historial de navegador (adelante/atrás).
"""
import os
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class Historial:
    def __init__(self):
        self.head = None
        self.current = None
        
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            self.current = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.current = new_node
        
    def print_historial(self):
        if not self.head:
            print("╔══════════════════════════════════")
            print("Historial vacio...")
            print("╚══════════════════════════════════")
            return
        
        current = self.head
        print("Historial: ")
        print("╔══════════════════════════════════")
        while current:
            if current == self.current:
                print(f"[{current.data}]")
                break
            else:
                print(current.data, end= " -> ")
            current = current.next
        print("╚══════════════════════════════════")
        print("\n╔══════════════════════════════════")
        print(f"║Accion actual: {self.current.data}")
        print("╚══════════════════════════════════")
        
    # Deshacer (undo)
    def undo_historial(self):
        if not self.head:
            print("Historial vacio...")
            return
        if self.current and self.current.prev:
            self.current = self.current.prev
        else:
            print("No hay más acciones para deshacer...")

        
        
    # Rehacer (endo)
    def endo_historial(self):
        if not self.head:
            print("Historial vacio...")
            return
        if self.current.next:
            self.current = self.current.next
        else:
            print("No hay acciones para rehacer...")
        
def menu():
    lista: Historial = Historial()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Histrial de acciones")
        lista.print_historial()
        print("Opciones de navegacion")
        print("1. Agregar Accion")
        print("2. Deshacer")
        print("3. Rehacer")
        print("4. Salir") 
        opc = input("Seleccione: ") 
        match opc:
            case "1":
                accion = input("Ingrese la accion: ")
                lista.append(accion)
                os.system("pause")
            case "2":
                lista.undo_historial()
                os.system("pause")
            case "3":
                lista.endo_historial()
                os.system("pause")
            case "4":
                print("Saliendo...") 
                break
            case _:
                print("Opción inválida")  
                os.system("pause")   
        
def main():
    menu()
    
    
if __name__ == "__main__":
    main()