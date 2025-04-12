"""
Insertar al principio y al final
Crea métodos para insertar un nodo al inicio y otro al final de la lista.
Métodos:
    append()
    prepend()
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def method_append(self, data):
        # Agregar al final de la lista #
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def method_prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def impresion(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
def main():
    lista: LinkedList = LinkedList()
    lista.method_append(5) # Al final de la lista
    lista.method_prepend(1) # Al inicio de la lista
    lista.impresion()
    
if __name__ == "__main__":
    main()