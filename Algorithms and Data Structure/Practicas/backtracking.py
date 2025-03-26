"""
Resolver un laberinto con backtracking y una pila
Se tiene un laberinto representado en una matriz y se debe encontrar una salida.
Representaci´pon del laberinto:
0 - Pared
1 - Camino
"S" - Salida
"E" - Entrada
"""

from collections import deque

# Laberinto
maze = [
    ["S", 1, 0, 1, "E"],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

# Movimientos posibles (derecha, izquierda, abajo, arriba)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_start(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "S":
                return (i, j)

def backtrack_maze(maze):
    start = find_start(maze)
    stack = deque([start])
    visited = set()
    
    while stack:
        x, y = stack.pop() # Obtener la posición actual
        
        if maze[x][y] == "E":
            print("Salida encontrada")
            return True
        
        visited.add((x, y))
        
        for dx, dy in moves:
            nx = x + dx                        
            ny = y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visited:
                stack.append((nx, ny))
                
    print("No hay salida")
    return False


backtrack_maze(maze) 
