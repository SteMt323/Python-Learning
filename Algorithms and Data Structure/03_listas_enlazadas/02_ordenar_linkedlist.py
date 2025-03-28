"""
Implementa una función en Python que reordene una 
lista enlazada de tal forma que los nodos con valores pares 
se muevan antes que los nodos con valores impares, pero manteniendo
el orden relativo de aparición de cada grupo.

Ejemplo:
head -> 1 -> 4 -> 3 -> 2 -> 5 -> 6 -> None

El output:
head -> 4 -> 2 -> 6 -> 1 -> 3 -> 5 -> None

Requisitos
    1. Implementar la clase Node y LinkedList
    2. Agregar un método reordenar_pares_impares()
    3. No crear una nueva lista, debes modificar la original
    4. Mantener el orden relativo de cada grupo (pares e impares)
    
Pistas
    - Usa dos punteros (pares y impares)
    - Separa los nodos en dos listas temporales (una para los pares
    y otra para los impares)
    - Une la lista de pares con la lista de impares al final
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        """Imprime la lista enlazada."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reordenar_pares_impares(self):
        """Reorganiza la lista enlazada para que los pares vayan antes de los impares."""
        # Implementa la solución aquí
        pares_head = None
        impares_head = None
        pares_tail = None
        impares_tail = None
        
        temp = self.head
        while temp:
            if temp.data % 2 == 0:
                if not pares_head:
                    pares_head = temp
                    pares_tail = temp
                else:
                    pares_tail.next = temp
                    pares_tail = temp
            else:
                if not impares_head:
                    impares_head = temp
                    impares_tail = temp
                else:
                    impares_tail.next = temp
                    impares_tail = temp
            
            temp = temp.next
            
        if pares_tail:
            pares_tail.next = impares_head
        if impares_tail:
            impares_tail.next = None
            
        self.head = pares_head
        

        

# Prueba el código
lista = LinkedList()
for num in [1, 4, 3, 2, 5, 6]:
    lista.append(num)

print("Lista Original:")
lista.print_list()

lista.reordenar_pares_impares()

print("Lista Reordenada:")
lista.print_list()
