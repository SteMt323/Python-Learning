"""
Eliminar un nodo por valor
Escribe una función que elimine el primer nodo que contenga un 
valor específico
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
        
        
    def eliminar_nodo(self, data):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.head
        if current.data == data:
            self.head = current.next  
            current = None
            
        prev = None
        while current.data != data:
            prev = current
            current = current.next
            
        prev.next = current.next
        current = None      
               
def main():
    lista: LinkedList = LinkedList()
    lista.agregar_datos(1)
    lista.agregar_datos(2)
    lista.agregar_datos(3)
    lista.agregar_datos(4)
    lista.agregar_datos(5)
    print("Lista original: ")
    lista.impresion()
    
    
    lista.eliminar_nodo(3)
    print("Nueva lista: ")
    lista.impresion()
    
if __name__ == "__main__":
    main()