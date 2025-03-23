### Números Primos ###

"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def es_primo(num):
    if num < 2:
        return False  # Los números menores que 2 no son primos.
    
    # Comprobamos si num es divisible por algún número entre 2 y num-1
    for i in range(2, num):
        if num % i == 0:  # Si el resto es 0, no es primo
            return False
    
    return True  # Si no se encuentra ningún divisor, es primo.

# Imprimimos los números primos entre 1 y 100
for i in range(1, 101):
    if es_primo(i):
        print(i)
