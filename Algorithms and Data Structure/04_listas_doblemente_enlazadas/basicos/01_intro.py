class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        new_node.prev = current # referenciar el nodo actual al nuevo nodo
        
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head # El nuevo nod apunta hacia adelante al nodo que era el head
        self.head.prev = new_node # El nodo que era head apunta hacia atrás al nuevo nodo
        self.head = new_node # Actualizamos el head
        
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev: # Si tiene un nodo anterior
                    current.prev.next = current.next # Ese nodo anterior debe apuntar al siguiente
                else: # Sino tiene nodo anterior es la cabeza
                    self.head = current.next # Se actualiza la cabeza al nodo siguiente
                
                if current.next: # Si tiene un siguiente nodo
                    current.next.prev = current.prev # Ese siguiente debe apuntar hacia atras al anterior
                return
            current = current.next
            
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(current.data)
            current = current.next
        
    def print_forward(self):
        current = self.head
        if not self.head:
            print("Lista vacia...")
            return 
        
        while current:
            print(current.data, end= " <-> ")
            current = current.next
        print("None")
        
    def print_back(self):
           current = self.head
           if not self.head:
               print("Lista vacia...")
               return
           
           # Llegar hasta el ultimo nodo
           while current.next:
               current = current.next
               
           
           # Recorrer la lista desde el ultimo nodo mediante prev
           while current:
                print(current.data, end= " <-> ")
                current = current.prev
           print("None")
        
def main():
    lista:DoubleLinkedList = DoubleLinkedList()
    
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)
    lista.append(6)
    
    lista.print_forward()
    lista.print_back()
    
    lista.delete(5)
    lista.print_forward()
    
if __name__ == "__main__":
    main()