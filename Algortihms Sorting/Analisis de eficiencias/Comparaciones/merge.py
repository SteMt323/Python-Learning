import sys
import time
import tracemalloc

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

def cargar_datos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return [int(linea.strip()) for linea in archivo.readlines()]
    
def main():
    if len(sys.argv) < 2:
        print("Uso: python ordenar.py <nombre_archivo>")
        sys.exit(1)

    archivo = sys.argv[1]
    datos = cargar_datos(archivo)
    
    tracemalloc.start()
    
    inicio = time.time()
    merge_sort(datos)
    fin = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    
    print(f"\n\nTiempo de ejecución: {fin-inicio:.4f} segundos")
    print(f"Memoria usada: {current / 1024:.6f} KB")
    print(f"Pico de memoria: {peak / 1024:.6f} KB")
    
    tracemalloc.stop()
    
if __name__ == "__main__":
    main()