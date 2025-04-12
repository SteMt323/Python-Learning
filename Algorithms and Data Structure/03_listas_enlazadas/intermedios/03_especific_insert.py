"""
Insertar en una posición específica
Crea un método que inserte un nodo en la posición k.
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
        
    def insert_position(self, k, data):
        new_node = Node(data)
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next

        if k == 0 and k == 1:
            new_node.next = self.head
            self.head = new_node
            return
            
        elif k > counter:
            print(f"Index Error, la posición {k} está fuera de rango")
            return
        
        else:
            current = self.head
            new_counter = 0
            while current:
                if new_counter == (k - 1):
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
                new_counter += 1
        
def main():
    lista: LinkedList = LinkedList()
    lista.agregar_datos(1)
    lista.agregar_datos(2)
    lista.agregar_datos(3)
    lista.agregar_datos(4)
    lista.agregar_datos(5)
    print("Lista original: ")
    lista.impresion()
    
    print("Lista nueva")
    lista.insert_position(1, 7)
    lista.impresion()
    
if __name__ == "__main__":
    main()