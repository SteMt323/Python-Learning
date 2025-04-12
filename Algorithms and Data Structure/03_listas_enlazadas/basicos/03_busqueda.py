"""
Buscar un valor
Crear un método que devuelva True o Fasle si un valor está presente 
en la lista.
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
        
    def buscar_valor(self, data):
        if not self.head:
            print("La lista esta vacia....")
            return 
        
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False
            
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
    n = int(input("Ingrese valor a buscar: "))
    print(lista.buscar_valor(n))
    
if __name__ == "__main__":
    main()
            
        
        
            