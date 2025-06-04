### Colas / Queues ###

"""
Una cola es una estructura de datos donde los elementos se procesan en orden 
FIFO (First In, First Out). Esto significa que el primer elemento que se añade
a la cola es el primero en ser eliminado.
"""

# Como declarar una cola
cola = []

cola.append(1)
cola.append(2)
cola.append(3)
print(cola) # [1, 2, 3]

cola.pop(0) # Elimina el primer elemento
# Nota: pop(0) para determinar la primera posicion de la cola
print(cola) # [2, 3]

"""
CUANDO USAR COLAS EN LUGAR DE PILAS Y LISTAS
1 - Algoritmos de impresión (Print Queue)
2 - Algoritmos de búsqueda en anchura (BFS)
3 - Algoritmos de simulación (Ej: Procesos en un sistema operativo)
4 - Algoritmos de ordenación (Ej: Invertir Datos)
5 - Algoritmos de Backtracking
"""

"""
Uso de collections.deque como cola
"""
from collections import deque

cola1 = deque()
cola1.append(1)
cola1.append(2)
cola1.append(3)
print(cola1) # deque([1, 2, 3])

cola1.popleft() # Elimina el primer elemento
print(cola1) # deque([2, 3])


