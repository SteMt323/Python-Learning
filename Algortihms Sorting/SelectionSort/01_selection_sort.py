### Selection Sort ###
"""
1. De qué trata:
  Encuentra el elemento más pequeño y lo coloca al inicio, luego 
  repite el proceso con el resto. 
  
2. Caso de uso: 
    Bueno para arreglos pequeños cuando el consumo de memoria 
    debe ser mínimo.
    
3. Comportamiento:
    O(n²) en todos los casos.

Visite la siguiente página para visualizar de manera gráfica
estos algortimos:
    https://visualgo.net/en/sorting
"""

lista = [5, 2, 10, 8, 23, 1, 0]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i # Elemento con menos valor
        for j in range(i + 2, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambio 
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr

print(selection_sort(lista))