"""
Sistema de canciones (playlist)
- Agrega canciones a una lista circular.
- Avanzar a la siguiente canción.
- Retroceder a la anterior.
- Eliminar canción actual.
- Mostrar la lista empezando desde la canción actual.
"""
import os
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.current = new_node
            return
            
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node
        self.current = new_node
        
    def print_playlist_from_current(self):
        if not self.head:
            print("Sin canciones...")
            return
        
        current = self.head
        while current:
            if current == self.current:
                break
            current = current.next
        while True:
            print(current.data, end = "\n")
            current = current.prev
            if current == self.current:
                break

        print(f"\nCancion Actual: {self.current.data}")
        
    def move_fordward(self):
        if not self.head:
            print("Sin canciones...")
            return
        
        current = self.head
        while current:
            if current == self.current:
                self.current = current.next
                return
            current = current.next
        print("No se puede avanzar...")
        
    def move_backward(self):
        if not self.head:
            print("Sin canciones...")
            return
        
        current = self.head
        while current:
            if current == self.current:
                self.current = current.prev
                return
            current = current.prev 
        print("No se puede retroceder...") 
        
    def delete_current_song(self):
        if not self.head:
            print("Sin canciones...")
            return
        
        current = self.head
        # Si solo hay un nodo
        if current.next == current and current.prev == current:
            self.head = None
            self.tail = None
            self.current = None
            return
        
        # Mas de un nodo
        # Evaluamos si el self.current es el head
        if current == self.current:
            next_node = self.head.next
            self.head = next_node
            self.head.prev = self.tail
            self.tail.next = self.head
            self.current = next_node
            return
        
        # Evaluamos si l self.current es la tail
        if self.current == self.tail:
            prev_node = self.tail.prev
            prev_node.next = self.head
            self.head.prev = prev_node
            self.tail = prev_node
            self.current = self.head
            return
        
        # Evaluamos los demas casos
        next_node = self.current.next
        prev_node = self.current.prev    

        prev_node.next = next_node
        next_node.prev = prev_node
        self.current = next_node
           

def menu():
    playlist: PlayList = PlayList()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("EDITOR DE TEXTO")
        print("1. Agregar Cancion")
        print("2. Avanzar")
        print("3. Retroceder")
        print("4. Eliminar Cancion Actual")
        print("5. Mostrar listado de Canciones")
        print("6. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                music = input("Ingrese una musica: ")
                playlist.append(music)
                os.system("pause")
                
            case "2":
                playlist.move_fordward()
                os.system("pause")
                
            case "3":
                playlist.move_backward()
                os.system("pause")
                
            case "4":
                playlist.delete_current_song()
                os.system("pause")
                
            case "5":
                playlist.print_playlist_from_current()
                os.system("pause")
            case "6":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida... intente nuevamente")
                os.system("pause")
                
                
def main():
    menu()
    
if __name__ == "__main__":
    main()