"""
Juego de cartas
Simula una mano de cartas:
- Agregar cartas al inicio o final.
- Eliminar la carta del medio.
- Reordenar la mano.
- Rotar la mano (hacer que la cabeza se vuelva la cola y viceversa).
"""
import os

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class Card_Maze: 
    def __init__(self):
        self.head = None
        
    # Agregar al final
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def prepend(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
    def print_maze(self):
        if not self.head:
            print("No hay cartas en el mazo...")
            return
        
        current = self.head
        counter = 1
        while current:
            print(f"Carta {counter}: {current.data}", end="\n")
            counter += 1
            current = current.next
        
    def delete_middle(self):
        if not self.head:
            print("No hay cartas en el mazo...")
            return
        
        current = self.head
        counter = 0
        while current:
            counter += 1           
            current = current.next
            
        if counter == 1:
            self.head = None
            return
        
        middle_node: int = counter//2
        current = self.head
        pos = 0
        while current:
            if pos == middle_node:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
            pos += 1
                
    def resorted_maze(self):
        if not self.head:
            print("No hay cartas en el mazo...")
            return
        
        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    changed = True
                current = current.next
                
    def rotate_maze(self):
        if not self.head:
            print("No hay cartas en el mazo...")
            return
        
        current = self.head
        next_node = None 
        previous_node = None
        while current:
            next_node = current.next 
            current.next = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node
        
def menu():
    card_maze: Card_Maze = Card_Maze()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        card_maze.print_maze()
        print("LISTA DE TAREAS")
        print("1. Agregar Carta al Inicio")
        print("2. Agregar Carta al Final")
        print("3. Eliminar Carta del Medio")
        print("4. Reordenar Mazo")
        print("5. Rotar Mazo")
        print("6. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                card = int(input("Ingrese el numero de la carta: "))
                card_maze.prepend(card)
                    
            case "2":
                card = int(input("Ingrese el numero de la carta: "))
                card_maze.append(card)
                
            case "3":
                card_maze.delete_middle()
                
            case "4":
                card_maze.resorted_maze()

            case "5":
                card_maze.rotate_maze()

            case "6":
                print("Saliedo...")
                break
            
            case _:
                print("Opción inválida, intente nuevamente...")
                os.system("pause")                
                
                
def main():
    menu()
    
if __name__ == "__main__":
    main()
        