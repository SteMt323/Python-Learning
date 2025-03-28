### Listas Enlazadas ###
"""
Una lista enlazada es una estructura de datos en la que los 
elementos están almacenados en nodos. Cada uno contiene:
1. Un valor (los datos que queremos almacenar)
2. Una referencia (puntero) al siguiente nodo de la lista.

Implementración de una Singly Linked List
Operaciones básicas de las listas enlazadas: 
- Agregar el nodo inicial
- Agregar el nodo final
- Buscar un nodo
- Eliminar un nodo
- Imprimir la lista
"""

class Node:
    """Clase que representa un nodo en la lista enlazada"""
    def __init__(self, data):
        self.data = data # Dato del nodo
        self.next = None # Puntero al siguiente nodo
        
class LinkedList:
    """Clase que representa la lista enlazada"""
    def __init__(self):
        self.head = None # Inicio de la lista (cabeza / head)
        
    def append(self, data):
        """Agrega un nodo al final de la lista"""
        new_node = Node(data) # Inicializa el constructor
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next # Avanzamos hasta el último nodo 
        temp.next = new_node # Enlazamos el nuevo nodo al final
        
    def prepend(self, data):
        """Agregamos un nodo al inicio de la lista"""
        new_node = Node(data)
        new_node.next = self.head # El nuevo nodo apunta a la cabeza actual
        self.head = new_node # La cabez ahora es el nuevo nodo
        
    def delete(self, key):
        """Elimina un nodo con un valor específico"""
        temp = self.head
        
        # Si la cabeza es el nodo a eliminar 
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        # Buscar el nodo a eliminar
        prev = None
        while temp and temp.data != key:
            prev = temp 
            temp = temp.next
            
        if not temp:
            return
        
        prev.next = temp.next
        temp = None
        
    def search(self, key):
        """Busca un nodo con un valor específico y retorna True o False"""
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def print_lista(self):
        """Imprime la lista enlazada"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
# Prueba de la lista
if __name__ == "__main__":
    linked_list = LinkedList() # Inicializa el constructor
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(0)
    linked_list.print_lista() # Imprime la lista 
    
    linked_list.delete(2)  # Elimina el nodo que contiene el elemento 2
    linked_list.print_lista()
    
    # Busca el nodo con el elemento especificado y retorna True o False
    print(linked_list.search(3)) # True
    print(linked_list.search(4)) # False