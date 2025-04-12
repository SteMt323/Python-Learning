"""
Imprimir en orden inverso sin modificarla
Usa recursión para imprimir los elementos de atrás hacia adelante 
sin alterar la estructura.
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
        
    def inverse_list(self):
        if not self.head:
            print("Lista vacia...")
            return
        temp = self.head
        
        def recursion_list(node):
            if node is None:
                return
            recursion_list(node.next)
            print(node.data, end="->")
            
        recursion_list(temp)
        
        
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
    lista.inverse_list()

    
if __name__ == "__main__":
    main()