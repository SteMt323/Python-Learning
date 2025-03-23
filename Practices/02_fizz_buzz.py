### FIZZ BUZZ ###
"""
El Famoso FIZZ BUZZ 
Escribe un programa que muestre por consola (con print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre 
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos dee 5 por la palabra "buzz".
- Múltiplos de 3 y 5 a la vez por la palabra "fizz buzz".
"""

my_list = [i+1 for i in range(100)]

def fizz_buzz(n = []):
    for i in n:
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - fizz buzz")
        elif i % 3 == 0:
            print(f"{i} - fizz")
        elif i % 5 == 0:
            print(f"{i} - buzz")
        else: 
            print(i)
    
fizz_buzz(my_list)