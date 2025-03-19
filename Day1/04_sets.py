### Sets ###

"""
Los sets son una colección de datos mutables que no garantizan un orden en especifico
en el mejor de los casos se usan cuando se requieren datos únicos (no repetidas)
y sin importar el orden.
"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario al ser declarado con {}

my_other_set = {"Steven", "Mejia", 18}
print(type(my_other_set))

my_other_set.add("StvM") # Guarda los elementos de manera desordenada
print(my_other_set) 

my_other_set.add("Steven") # Un set no admite repetidos 
print(my_other_set)

print("Mam" in my_other_set) # Para determinar si el dato existe en mi set
print("Steven" in my_other_set)

