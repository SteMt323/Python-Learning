import sys
import time
import tracemalloc

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
    insertion_sort(datos)
    fin = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    
    print(f"\n\nTiempo de ejecución: {fin-inicio:.4f} segundos")
    print(f"Memoria usada: {current / 1024:.6f} KB")
    print(f"Pico de memoria: {peak / 1024:.6f} KB")
    
    tracemalloc.stop()
    
if __name__ == "__main__":
    main()