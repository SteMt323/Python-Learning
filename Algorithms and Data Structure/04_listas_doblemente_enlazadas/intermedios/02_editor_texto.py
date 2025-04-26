"""
1. Editor de texto simplificado
Simula un editor donde puedas:

- Insertar caracteres.
- Mover el cursor hacia adelante o atrás.
- Borrar (como un backspace).
- Mostrar el texto actual.
Cada carácter es un nodo. ¡Ideal para practicar prev y next!
"""
import os

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class TextEditor:
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
        
    def impresion(self):
        if not self.head:
            print("No hay caracteres ingresados...")
            return
        
        current = self.head
        print("\nTexto")
        while current:
            print(current.data, end=" ")
            current = current.next
        print(f"\nCaracter actual: {self.current.data}\n")
        
    def move_current_fordward(self):
        if not self.head:
            print("No hay caracteres ingresados...")
            return
        
        current = self.head
        while current:
            if current.next and current == self.current:
                self.current = current.next
                return
            current = current.next
        print("No se puede mover hacia adelante.")
            
    def move_current_backward(self):
        if not self.head:
            print("No hay caracteres ingresados...")
            return
        
        current = self.head
        while current:
            if current.prev and current == self.current:
                self.current = current.prev
                return
            current = current.next
        print("No se puede mover hacia atras")
            
    def delete_current_data(self):
        if not self.head:
            print("No hay caracteres ingresados...")
            return
        
        node_delete = self.current
        
        current = self.head
        if self.head == node_delete:
            self.head = current.next
            self.current = current.next
            return
        
        while current.next:
            prev_node = current
            current = current.next
        if not current.next and current == node_delete:
            self.current = prev_node
            prev_node.next = None
            current = None
            return
        
        current = self.head
        while current.next:
            prev_node = current.prev
            next_node = current.next
            if current == node_delete:
                prev_node.next = next_node
                next_node.prev = prev_node
                self.current = prev_node
                current = None
                return
            current = current.next
        print("No se ha eliminado el nodo")
        
def menu():
    text_editor: TextEditor = TextEditor()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        text_editor.impresion()
        print("EDITOR DE TEXTO")
        print("1. Insert char")
        print("2. Move Forward")
        print("3. Move Backward")
        print("4. Delete current")
        print("5. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                char = input("Ingrese un caracter: ")
                if len(char) == 1:
                    text_editor.append(char)
                    os.system("pause")
                else: 
                    print("Solo un caracter, intente denuevo...")
                    os.system("pause")
                
            case "2":
                text_editor.move_current_fordward()
                os.system("pause")
                
            case "3":
                text_editor.move_current_backward()
                os.system("pause")
                
            case "4":
                text_editor.delete_current_data()
                os.system("pause")
                
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida... intente nuevamente")
                os.system("pause")
                
                
def main():
    menu()
    
if __name__ == "__main__":
    main()
        