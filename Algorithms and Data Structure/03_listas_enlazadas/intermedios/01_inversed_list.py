"""
Invertir la lista
Escribe una función que invierta la lista enlazada (cambiando los puntreros)
"""

class Node:
    def __init__(self, data):
        self.next = None 
        self.data = data
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def agregar_datos(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def impresion(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
    def invertir_lista(self):
        if not self.head:
            print("Lista vacia... ")
            return
        
        temp = self.head
        prev = None
        next_node = None
        
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

            
            
            
        
def main():
    lista: LinkedList = LinkedList()
    lista.agregar_datos(1)
    lista.agregar_datos(2)
    lista.agregar_datos(3)
    lista.agregar_datos(4)
    lista.agregar_datos(5)
    print("Lista original: ")
    lista.impresion()
    
    print("Lista inversa: ")
    lista.invertir_lista()
    lista.impresion()
    
if __name__ == "__main__":
    main()