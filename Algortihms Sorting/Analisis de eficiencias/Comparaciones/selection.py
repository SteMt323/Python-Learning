import sys
import time
import tracemalloc

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
    selection_sort(datos)
    fin = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    
    print(f"\n\nTiempo de ejecución: {fin-inicio:.4f} segundos")
    print(f"Memoria usada: {current / 1024:.6f} KB")
    print(f"Pico de memoria: {peak / 1024:.6f} KB")
    
    tracemalloc.stop()
    
if __name__ == "__main__":
    main()