"""
Revertir una lista
- Implementa un método que invierta el orden de los nodos.
- Sin usar estructuras auxiliares (solo moviendo next y prev).
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
            self.head = new_node
            self.tail = None
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.tail = new_node
        
    def print_list(self):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.head
        while current:
            print(current.data, end="\n")
            current = current.next
            
    def reverse_list(self):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.head
        next_node = None 
        previous_node = None
        while current:
            next_node = current.next 
            current.next = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node
        self.tail = next_node
        
def main():
    lista: DoubleLinkedList = DoubleLinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)
    print("Lista original: ")
    lista.print_list()
    print("\nLista inversa: ")
    lista.reverse_list()
    lista.print_list()
    
if __name__ == "__main__":
    main()
    