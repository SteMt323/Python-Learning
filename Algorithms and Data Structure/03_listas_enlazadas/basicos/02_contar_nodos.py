"""
Contar nodos 
Escribe una función que cuente la cantidad de nodos en la lista.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
        
    def count_nodes(self):
        if not self.head:
            print("La lista esta vacía...")
            return
        
        temp = self.head
        counter = 1
        while temp.next:
            counter += 1
            temp = temp.next
        return counter
    
    def impresion(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
    
def main():
    lista: LinkedList = LinkedList()
    lista.agregar_datos(1)
    lista.agregar_datos(2)
    lista.agregar_datos(3)
    lista.agregar_datos(4)
    lista.agregar_datos(5)
    lista.impresion()
    print(lista.count_nodes())
    
if __name__ == "__main__":
    main()