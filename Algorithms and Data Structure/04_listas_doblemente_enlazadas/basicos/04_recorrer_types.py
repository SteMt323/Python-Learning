"""
Recorrer de adelante hacia atrás y de atrás hacia adelante.
"""
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class DoubleLinkedList():
    def __init__(self):
        self.head = None
        
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
        
    def print_forward(self):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def print_back(self):
        if not self.head:
            print("Lista vacia...")
            return
        current = self.head
        while current.next:
            current = current.next
            
        temp = current
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
        
def main():
    lista: DoubleLinkedList = DoubleLinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)
    print("Impresion hacia adelante: ")
    lista.print_forward()
    print("Impresion hacia atras: ")
    lista.print_back()
    
if __name__ == "__main__":
    main()