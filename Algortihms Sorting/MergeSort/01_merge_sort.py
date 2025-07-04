### Insertion Sort ###
"""
1. De qué trata:
  Divide la lista en mitades, ordena cada mitad y luego las 
  combina de forma ordenada.
  
2. Caso de uso: 
    Cuando se requiere una eficiencia garantizada, sin importar 
    el estado inicial de los datos.
    
3. Comportamiento:
    O(n log n) en todos los casos.

Visite la siguiente página para visualizar de manera gráfica
estos algortimos:
    https://visualgo.net/en/sorting
"""
import tracemalloc 
import time as tm

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Encontrar el punto medio
        # Dividir en dos mitades
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left) # Ordena mitad izquierda
        merge_sort(right) # Ordena mitad izquierda
        
        i = j = k = 0
        # Fusionar las mitades ordenadamente
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left): # Agrega los elementos restantes a la izquierda
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):  # Agrega los elementos restantes de la derecha
            arr[k] = right[j]
            j += 1
            k += 1
                
    return arr


lista = list(x for x in reversed(range(0, 100000)))

tracemalloc.start()
start = tm.time()
merge_sort(lista)
end = tm.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"TIEMPO: {end - start} segundos")
print(f"Memoria actual usada: {current / 10**6:.2f} MB")
print(f"Pico de memoria usado: {peak / 10**6:.2f} MB")