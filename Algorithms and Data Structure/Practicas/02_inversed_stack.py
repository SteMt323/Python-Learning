"""
Escriba un programa que invierta una cadena de texto utilizando una pila.
- Pasa cada carácter de la cadena a la pila.
- Luego, vacía la pila, imprimioendo los caracteres de manera inversa.
"""
from collections import deque

def reverse_string(text):
    stack = deque()
    for i in text:
        stack.append(i)
        
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()
    return reversed_text

def main():
    text = "Hola Mundo"
    print(reverse_string(text))
    
if __name__ == "__main__":
    main() 

