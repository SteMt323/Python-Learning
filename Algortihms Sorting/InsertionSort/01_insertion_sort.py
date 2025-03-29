### Insertion Sort ###
"""
1. De qué trata:
  Recorre la lista y va insertando cada elemento en su posición 
  correcta.
  
2. Caso de uso: 
    Útil cuando la lista ya está casi ordenada o cuando se 
    ordenan datos en tiempo real.
    
3. Comportamiento:
    O(n²) en el peor caso, pero O(n) en listas casi ordenadas.

Visite la siguiente página para visualizar de manera gráfica
estos algortimos:
    https://visualgo.net/en/sorting
"""
lista = [5, 3, 8, 6, 2]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(lista))