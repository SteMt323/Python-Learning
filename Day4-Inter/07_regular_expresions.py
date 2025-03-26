### Expresiones Regulares ###

"""
Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda. Permiten realizar búsquedas de cadenas de texto más complejas.
Por ejemplo: buscar todas las palabras que empiecen con "a" o buscar todas las palabras que contengan un número.
"""

import re

my_string = "Ejemplo para visualizar las expresines regulares en Python"

match = re.match("Ejemplo para", my_string)
print(match)
start, end = match.span()
print(my_string[start:end])


# Empieza a buscar desde el principio de la cadena
print(re.match("Ejemplo para", my_string))

