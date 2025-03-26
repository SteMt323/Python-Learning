### Pilas / Stack ###

"""
Una pila es una estructura de datos que sigue el principio de LIFO (Last In, First Out).
Esto significa que el último elemento que se añade a la pila es el primero en 
ser eliminado.
En otras palabras, es como una pila de platos: el último plato que se coloca en la pila
es el primero en ser retirado.
"""

# Como declarar una pila
pila = []

# Push (añadir elementos)
pila.append(1)
pila.append(2)
pila.append(3)

# Pop (quitar el último elemento)
ultimo = pila.pop()
# Nota: pop() sin argumentos elimina el último elemento de la pila
print(ultimo) # 3

# Peek (ver el último elemento sin quitarlo)
ultimo = pila[-1]
print(ultimo) # 2

"""
CUANDO USAR PILAS EN LUGAR DE COLAS

1 - Algoritmos de Deshacer y Rehacer (Undo/Redo)
2 - Recorrido en profundidad de un grafo o árbol(DFS)
    - En algoritmos de búsqueda en profundidad, se suele usar una pila para almacenar
      los nodos que se van visitando.
3 - Validación de expresiones matemáticas
4 - Llamadas recursivas (Pila de ejecución)
5 - Algoritmos de Backtracking
"""


# Uso de collections.deque como pila
from collections import deque

"""
Pros:
- Las operaciones de inserción y eliminación son de complejidad O(1). 
- Se puede usar como pila o cola.

Contras:
- No se puede acceder a elementos arbitrarios. Es decir, no se puede hacer pila[0].
  Esto es debido a que es una estrucutra restrictiva que solo permite añadir y quitar
  elementos por los extremos.
"""

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) # deque([1, 2, 3])

stack.pop()
print(stack) # deque([1, 2])