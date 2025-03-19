### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [18, 22, 54, 69, 78, 22]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "StvM"]
print(my_other_list)

print(type(my_other_list))
print(type(my_list))

# Acceder a los valores de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])

print(my_list.count(22)) # Contar el número de una variable en especifico dentro de la lista

age, height, name = my_other_list
print(name)

my_other_list.append("Miau") # Insertar un elemento al final de la lista con el método append
print(my_other_list)

my_other_list.insert(1, "Morado") # Insertar un elemento en una posición especificada ("posición de la lista", "Elemento")
print(my_other_list)

my_other_list.remove("Morado") # Remover un elemento conocido de una lista
print(my_other_list)

del my_list[2] # Elimina un elementopor índice
print(my_list)


# División de listas  (sublistas)
print(my_list[0:3]) # Imprime los elementos desde el índice 0