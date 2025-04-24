"""
Invertir la lista doblemente enlazada
"""
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class DoubleLinkedList:
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
            
    def reverse_list(self):
        # no se usa recursion, el head aqui tiene que ser el tail, y el tail el head
        if not self.head:
            print("Lista vacía...")
            return
        
        current = self.head
        previous_node = None
        next_node = None
        while current:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node
        
def main():
    lista: DoubleLinkedList = DoubleLinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)
    print("Lista normal: ")
    lista.print_forward()
    print("\nLista inversa: ")
    lista.reverse_list()
    lista.print_forward()
    
if __name__ == "__main__":
    main()
    
            