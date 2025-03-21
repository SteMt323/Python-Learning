### Manejo de Excepciones / Exception Handing ###

# try except else finally 

try:                                
    # El bloque try intenta ejecutar el bloque de código, si se produce un error se captura con except
    num1 = int(input("Numero 1: "))
    num2 = int(input("Número 2: "))
    print("La suma de los dos números es: ", num1 + num2)
except Exception as e:
    # El bloque except se ejecuta cuando se captura algún error en la ejecución
    # "Exception" sirve para capturar cualquier tipo de excepcion y almacenarla en una variable
    print(f"Se ha producido un error: {e}") 
else: # Opcional
    # El bloque else se ejecuta cuando no se hayan producido errores
    print("Continuamos la ejecución") 
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecucuion continua") 
    
# Excepciones por tipo
try:                                
    num1 = int(input("Numero 1: "))
    num2 = int(input("Número 2: "))
    print("La suma de los dos números es: ", num1 + num2)
except ValueError as e: 
    # Informar sobre el error, capturando la excepcion mediante una variable
    print(f"Se ha producido un ValueError: {e}") 
    

name=input("Di tu nombre: ")

