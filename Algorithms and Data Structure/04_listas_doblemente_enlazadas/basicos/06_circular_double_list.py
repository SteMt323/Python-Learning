"""
Crear una lista doblemente circular.
"""
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node
        
    def print_forward(self):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print(" (circular) ")
        
    def print_back(self):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.tail
        while True:
            print(current.data, end = " <-> ")
            current = current.prev
            if current == self.tail:
                break
        print(" (circular) ")
        
def main():
    lista:DoubleLinkedList = DoubleLinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)
    print("Imprimir lista circular hacia adelante")
    lista.print_forward()
    print("\nImprimir lista circular hacia atras: ")
    lista.print_back() 
    
if __name__ == "__main__":
    main()