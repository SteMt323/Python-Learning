# Complejidad Algorítmica y Notación Big-O

La **complejidad algorítmica** describe el tiempo de ejecución o uso de memoria de un algoritmo en función del tamaño de la entrada (**n**). Se expresa con la **notación Big-O**.

## Tabla de Complejidades Comunes

| Notación | Nombre         | Descripción |
|-----------|---------------|-------------|
| **O(1)** | Constante     | No importa el tamaño de la entrada, el tiempo de ejecución es el mismo. |
| **O(log n)** | Logarítmica | El tiempo de ejecución crece lentamente a medida que la entrada aumenta. Ejemplo: Búsqueda binaria. |
| **O(n)** | Lineal        | El tiempo de ejecución crece proporcionalmente al tamaño de la entrada. |
| **O(n log n)** | Subcuadrática | Más eficiente que O(n²), usada en algoritmos como Merge Sort y Quick Sort. |
| **O(n²)** | Cuadrática    | El tiempo crece de manera cuadrática con la entrada. Ejemplo: Bubble Sort. |
| **O(2^n)** | Exponencial  | Crece extremadamente rápido, usado en problemas de backtracking. |
| **O(n!)** | Factorial    | La peor complejidad, usada en permutaciones y problemas de fuerza bruta. |

---

## Ejemplos en Python

### 1️⃣ O(1) - Constante
```python
# Siempre toma el mismo tiempo sin importar la entrada

def acceso_directo(arr, i):
    return arr[i]  # Operación en tiempo constante O(1)
```

### 2️⃣ O(n) - Lineal
```python
# Recorre toda la lista una vez

def recorrer_lista(arr):
    for x in arr:
        print(x)  # Se ejecuta 'n' veces
```

### 3️⃣ O(n²) - Cuadrática
```python
# Dos bucles anidados

def cuadratico(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Se ejecuta 'n²' veces
```

### 4️⃣ O(n log n) - Merge Sort
```python
# Algoritmo eficiente de ordenamiento

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
```

### 5️⃣ O(2^n) - Fibonacci Recursivo
```python
# Crecimiento exponencial

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Se llama a sí mismo dos veces
```

---

## 🚀 Conclusión
Elegir el algoritmo correcto es clave para mejorar el rendimiento. Si tienes una lista grande, evita O(n²) y busca soluciones O(n log n) o mejores.


