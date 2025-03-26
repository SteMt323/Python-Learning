### Recursividad ###
"""
Las funciones recursivas son aquellas que se llaman a sí mismas dentro 
de su propia definición para resolver un problema. Este tipo de 
funciones descomponen un problema en subproblemas más pequeños, hasta 
alcanzar un caso base que detiene la recursión.

En Python, la recursividad se usa en problemas que pueden dividirse en versiones 
más simples de sí mismos, como el cálculo de factoriales, la serie de Fibonacci y 
la búsqueda en estructuras de datos jerárquicas.

Características de las funciones recursivas:
1- Llamada recursiva: La función se llama a sí misma dentro de su definición.

2- Caso base: Una condición que detiene la recursión. Sin ella
la función recursiva se llamaría infino número de veces.

3- Descomposición del problema: El problema original se divide en subproblemas
más pequeños y manejables.
"""

# Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) # 120


# Serie de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(5)) # Resultado: (0, 1, 1, 2, 3, 5)



