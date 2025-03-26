from collections import deque

cola = deque()
cola.append("Documento 1")
cola.append("Imagen 2")
cola.append("Documento 3")
cola.append("Imagen 4")

print(cola)

print(cola.popleft())
print(cola)