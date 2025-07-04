"""
🧮 1. Calculadora mágica de operaciones raras
Un menú que te permite elegir entre operaciones matemáticas poco comunes:

Factorial de un número.

Serie de Fibonacci hasta n.

Verificar si un número es primo.

Suma de dígitos de un número.

Salir.

💡 Ideal para practicar while, for, funciones y validación numérica.
"""
import os

class Calculadora:
    def __init__(self):
        pass
    
    def factorial_num(self, num) -> int:
        result = 1
        for i in range(num, 0, -1):
            result *= i
        return result
    
    def fibonacci(self, ran) -> list:
        fib = [0, 1]
        for i in range(ran):
            fib.append(fib[i] + fib[i+1])
        return fib
    
    
    def primo(self, num):
        is_prim = False
        counter = 0
        for i in range(num):
            if num % (i+1) == 0: counter += 1
        if counter == 2:
            is_prim = True
        return is_prim
    
    def sum_digits_num(self, num):
        num = str(num)
        list_num = []
        for i in num:
            list_num.append(int(i))
        return sum(list_num)
            
    
def menu():
    cal: Calculadora = Calculadora()
    while True:
        print("\n\n___ Calculadora de Operaciones poco Usuales ____")
        print("1. Factorial de un número")
        print("2. Serie Fibonacci hasta n")
        print("3. Verificar numero primo")
        print("4. Suma de digitos de un numero")
        print("5. Salir")
        opc = input("Elija una opción: ")
        match opc:
            case "1":
                while True:
                    num = input("Ingrese el numero: ")
                    if num.isdigit(): 
                        num = int(num)
                        break
                    else: print("Opcion invalida...")
                print(f"Factorial del numero {num} es: {cal.factorial_num(num)}")
                os.system("pause")
            case "2":
                while True:
                    num = input("Ingrese el numero: ")
                    if num.isdigit(): 
                        num = int(num)
                        break
                    else: print("Opcion invalida...")
                print(f"Serie Fibonnaci hasta el {num} es: {cal.fibonacci(num)}")
                os.system("pause")
            case "3":
                while True:
                    num = input("Ingrese el numero: ")
                    if num.isdigit(): 
                        num = int(num)
                        break
                    else: print("Opcion invalida...")
                print(f"El {num} es número primo?: {"Es primo" if cal.primo(num) else "No es primo"}")
                os.system("pause")
            case "4":
                while True:
                    num = input("Ingrese el numero: ")
                    if num.isdigit(): 
                        num = int(num)
                        break
                    else: print("Opcion invalida...")
                print(f"La suma de los digitos del numero {num} es: {cal.sum_digits_num(num)}")
                os.system("pause")
            case "5": break
            case _: print("Opocion invalida...")
    
def main():
    menu()
    
if __name__ == "__main__":
    main()