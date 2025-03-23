### Funciones de orden superior ###

"""
Las funciones de orden superior son aquellas que reciben 
funciones como parámetros o devuelven funciones como resultado. 
El uso de lambda dentro de estas funciones hace que el código sea 
más conciso y fácil de leer para ciertas tareas.
"""



# Básico función dentro de función
def sum_one(x):
    return x + 1

def sum_plus_one(x, y, f):
    return f(x + y)

print(sum_plus_one(3, 4, sum_one))

### Closures ###
"""
Una closure es una función que devuelve otra función y esa función interna tiene 
acceso a las variables del contexto original, incluso cuando la función original 
ya ha terminado de ejecutarse. Este comportamiento permite que las variables 
internas sean privadas y no puedan ser modificadas directamente desde fuera, 
lo que ayuda a mantener el estado encapsulado y controlado.
"""
def sum_ten(value2):
    def add(value):
        return value + 10 + value2
    return add
    
add_closure = sum_ten(5)
print(add_closure(5))



### Funciones de orden superior propias del lenguaje ###
# map()
numbers = [2, 5, 3, 93, 34]

def mult(x):
    return x * 2

print(list(map(mult, numbers)))

# Con lambda
# Comprension de listas, potenciacion a los valores con map()
potenciacion_lista = list(map(lambda x: x**2, numbers))
print(potenciacion_lista)


# filter()
def filters(x):
    if x > 10:
        return True
    else:
        return False
    
print(list(filter(filters, numbers)))

# Con lambda
# Compresion de listas, filtro de valores con filter()
filtro_lista = list(filter(lambda x: x % 2 == 0, numbers))
print(filtro_lista)

