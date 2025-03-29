### Bubble Sort ###
"""
1. De qué trata:
  Compara elementos adyacentes y los intercambia si están en el 
  orden incorrecto. Repite este proceso hasta que la lista esté 
  ordenada.  
  
2. Caso de uso: 
    Cuando el conjunto de datos es pequeño y no se requiere 
    alta eficiencia.
    
3. Comportamiento:
    O(n²) en el peor caso, O(n) si la lista ya está ordenada.

Visite la siguiente página para visualizar de manera gráfica
estos algortimos:
    https://visualgo.net/en/sorting
"""

# Ejemplo
lista = [5, 2, 8, 10, 3, 2, 0, 9]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubble_sort(lista))