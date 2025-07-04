import sys
import time
import tracemalloc

def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(lo, hi):
        pivot = arr[hi]  
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        return i + 1

    if low < high:
        p = partition(low, high)
        quicksort_inplace(arr, low, p - 1)
        quicksort_inplace(arr, p + 1, high)

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
    quicksort_inplace(datos)
    fin = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    
    print(f"\n\nTiempo de ejecución: {fin-inicio:.4f} segundos")
    print(f"Memoria usada: {current / 1024:.6f} KB")
    print(f"Pico de memoria: {peak / 1024:.6f} KB")
    
    tracemalloc.stop()
if __name__ == "__main__":
    main()
