### Lambdas ###

# Condicional
condicional = lambda x, y: True if x > y else False
print(condicional(1,2))
# nombramos variable - llamamos palabra reservada - argumentos - "Valor si verdadero" if "Condición" else "Valor si no es verdadero"
def lambd_func(x,y):
    if x > y:
        return True
    else: 
        return False

# Operaciones 
suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y

print(suma(3, 5))  # 8
print(resta(10, 4))  # 6
print(multiplicacion(4, 7))  # 28
print(division(9, 3))  # 3.0

