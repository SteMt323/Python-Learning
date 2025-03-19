### Diccionarios ###
"""
Estructuras de datos organizadas por claves y valores (clave:valor)
"""
my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {"Nombre":"Steven", "Apellido":"Mejia","Edad":18, 1:"Python"}

my_dict = {
    "Nombre":"Steven", 
    "Apellido":"Mejia",
    "Edad":18, 
    "Lenguaje":{"Python", "Java", "Dart"}
    }

print(my_other_dict)
print(my_dict["Lenguaje"])