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
        return