"""
Eliminar un nodo dado (por valor o posición).
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
    
    # Eliminar por dato
    def delete_data(self, data):
        if not self.head:
            print("Lista vacia...")
            return
        # Eliminar en el head
        current = self.head
        if current.data == data:
            self.head = current.next
            current = None
            return
        
        # Eliminar en la tail
        while current.next:
            current = current.next
        previous_node = current.prev
        if current.data == data:
            previous_node.next = None
            current = None
            return
        
        # Eliminar en los demas
        current = self.head
        while current.next:
            previous_node = current.prev
            if current.data == data:
                previous_node.next = current.next
                current.prev = previous_node
                current = None
                return
            current = current.next
            
    def delete_index(self, index):
        if not self.head:
            print("Lista vacia...")
            return
        
        current = self.head
        counter = 0
        # Eliminar del head
        if counter == index:
            self.head = current.next
            current = None
            return
        
        # Eliminar del tail
        while current.next:
            counter += 1
            current = current.next
        previous_node = current.prev
        if counter == index:
            previous_node.next = None
            current = None
            
        # Eliminar en lo demas
        current = self.head
        secundary_counter = 0
        while current:
            previous_node = current.prev
            if secundary_counter == index:
                previous_node.next = current.next
                current.next = previous_node
                current = None
                return
                
            secundary_counter += 1
            current = current.next
        
    def print_forward(self):
        if not self.head:
            print("Lista vacía...")
            return
        current = self.head
        while current:
            print(current.data, end= " <-> ")
            current = current.next
        print("None")
        
def main():
    lista: DoubleLinkedList = DoubleLinkedList()
    lista.append(1)
    lista.append(3)
    lista.append(5)
    lista.append(7)
    lista.append(9)
    print("Lista original: ")
    lista.print_forward()
    print("Eliminar el dato 3: ")
    lista.delete_data(9)
    lista.print_forward()
    print("Eliminar el nodo de indice 2: ")
    lista.delete_index(2)
    lista.print_forward()
    
if __name__ == "__main__":
    main()
    