"""
Ejercicio: Eliminar elementos duplicados en una lista enlazada
Objetivo:
Dada una lista enlazada con números, debemos eliminar los nodos duplicados
de la lista. Los duplicados no deben repetirse en la lista, pero el orden original
debe mantenerse
Input:
1 -> 2 -> 3 -> 2 -> 4 -> 3 -> 5 -> None

Output:
1 -> 2 -> 3 -> 4 -> 5 -> None

Pasos para resolverlo: 
1. Usar un conjunto (set) para almacenar los valores que ya hemos encontrado.
   Esto nos ayudará a identificar los duplicados de manera eficiente.

2. Recorrer la lista enlazada y, por cada nodo:
    - Si su valor ya está en el conjunto, eliminamos el nodo (es decir, lo desconectamos
      de la lista)
    - Si no está en el conjunto, lo agregamos al conjunto y seguimos adelante.
    
3. Actualizar las referencias de los nodos para eliminar los duplicados sin afectar
   el orden de la lista.
"""

class Node:
    def __init__(self, data):
        self.data = data  # El valor del nodo
        self.next = None  # El siguiente nodo (referencia)

class LinkedList:
    def __init__(self):
        self.head = None  # Cabeza de la lista

    def append(self, data):
        """Añade un nuevo nodo al final de la lista."""
        new_node = Node(data)  # Creamos un nuevo nodo
        if not self.head:  # Si la lista está vacía
            self.head = new_node  # El nuevo nodo es la cabeza
            return
        temp = self.head
        while temp.next:  # Recorre hasta el final de la lista
            temp = temp.next
        temp.next = new_node  # Enlaza el nuevo nodo al final

    def print_list(self):
        """Imprime la lista enlazada."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def eliminar_duplicados(self):
        """Elimina los nodos duplicados de la lista enlazada."""
        # Tu código aquí
        seen = set()  # Conjunto para valores ya vistos
        temp = self.head  

        # Si la lista está vacía o solo tiene un nodo, no hay duplicados
        if not temp:
            return
        
        seen.add(temp.data)  # agregar el primer valor a 'seen'
        
        while temp and temp.next:
            if temp.next.data in seen:  # Si el siguiente nodo es un duplicado
                temp.next = temp.next.next  # Eliminarlo de la lista
            else:
                seen.add(temp.next.data)  # Si no es duplicado, agregarlo a 'seen'
                temp = temp.next  # Mover al siguiente nodo

# Prueba el código
lista = LinkedList()
for num in [1, 2, 3, 2, 4, 3, 5]:
    lista.append(num)

print("Lista Original:")
lista.print_list()

lista.eliminar_duplicados()

print("Lista Después de Eliminar Duplicados:")
lista.print_list()
