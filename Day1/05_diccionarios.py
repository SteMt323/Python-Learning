### Diccionarios ###
"""
Estructuras de datos organizadas por claves y valores (clave:valor)
"""
my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {"Nombre":"Steven", "Apellido":"Morgan","Edad":18, 1:"Python"}

my_dict = {
    "Nombre":"Steven", 
    "Apellido":"Morgan",
    "Edad":18, 
    "Lenguaje":{"Python", "Java", "Dart"}
    }

print(my_other_dict)
print(my_dict["Lenguaje"])

my_dict["Escuela"] = "Uam" # Para agregar nuevos elementos al diccionario
print(my_dict)

del my_dict["Escuela"] # Para eliminar un elemento en especifico del diccionario, a traves de la clave
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())



my_new_dict = dict.fromkeys(("Nombre", "Edad")) # Crea un nuevo diccionario sin valores
print(my_new_dict) 

