"""
Verificar si una cadena / string tiene paréntesis balanceados.
Escribe un programa que se use para verificar si una cadena de paréntesis
está balanceada. Los paréntesis deben abrirse y cerrarse en el orden correcto.
- Debe de usar Pilas / Stack
"""

from collections import deque

def balanced_parentheses(cadena):
    stack = deque()
    for i in cadena:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

            
def main():
    cadena = input("Introduce una cadena de paréntesis: ")
    if balanced_parentheses(cadena):
        print("Los paréntesis están balanceados")
    else:
        print("Los paréntesis no están balanceados")
        
if __name__ == "__main__":
    main()