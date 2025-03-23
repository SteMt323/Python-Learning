### La sucesión de Fibonacci ###
"""
Escribe un programa que imprima los primeros 50 números de la sucesión de 
Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el 
siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13 ...
"""

# Mi solución
def fibonacci():
    fib = [0, 1]
    for i in range(48):
        fib.append(fib[i] + fib[i+1])
    return fib

print(fibonacci())

# Sugerencia con ia
def fibonacci_ia(n=50):
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci_ia())
