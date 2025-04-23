"""
Insertar al principio, al final y en una posición específica.
"""
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class DoubleLinkedList():
    def __init__(self):
        self.head = None
        
    # Agregar al final 
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
        
    def prepend(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def especific_insert(self, index, data):
        new_node: Node = Node(data)

        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
            
        # Insercion en el head (un prepend)
        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return
            
        # Evaluar si el index esta fuera de rango
        if index > counter:
            print("Index fuera de rango...")
            return
        
        # Insertar en indice especifico (no el head ni la cola)
        current = self.head
        position = 0
        while current:
            if position == index: # Si posicion es el index
                previous_node = current.prev # guardamos en una variable temporal el nodo anterior de current
                
                new_node.prev = previous_node # el nodo anterior del nuevo nodo va a ser la variable temporal
                new_node.next = current # el siguiente nodo del nuevo nodo sera el nodo actual
                
                if previous_node: # Si la variable temporal agarro el nodo anterior del current
                    previous_node.next = new_node # Hacemos que el next del nodo anterior al current sea el nuevo nodo
                current.prev = new_node # actualizamos el nodo anterior de current para que sea el nuevo nodo
                return
                
            position += 1 # Si no se cumple la condicion, se le suma 1 a posicion
            current = current.next
            
        # Si llegamos al final de la lista (un append)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def print_forward(self):
        if not self.head:
            print("Lista vacía...")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
def main():
    lista: DoubleLinkedList = DoubleLinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    lista.prepend(1)
    
    lista.print_forward()
    print("\nInsersion del elemento (9) en el indice 2")
    lista.especific_insert(2, 9)
    lista.print_forward()
    
if __name__ == "__main__":
    main()