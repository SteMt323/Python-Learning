### Manejo de Ficheros ###
import os

# Modos de apertura de archivos:
# "r"  - Modo lectura. El archivo debe existir. Lanza un error si no se encuentra.
# "w"  - Modo escritura. Crea un archivo nuevo si no existe. Sobrescribe el contenido si ya existe.
# "x"  - Modo creación. Crea un archivo nuevo, pero lanza un error si ya existe.
# "a"  - Modo anexar. Escribe al final del archivo sin sobrescribir el contenido existente.
# "b"  - Modo binario. Se usa junto con otros modos para trabajar con archivos binarios.
# "t"  - Modo texto. Es el modo por defecto y se usa para trabajar con archivos de texto.
# "+"  - Modo lectura y escritura. Se combina con otros modos como "r+", "w+", "a+".


"""
Al momento de la escritura o lectura de un archivo, podemos usar la función 
seek() para mover el puntero a una posición específica del archivo o al
principio de este mismo.
"""

"""
.txt file
"""    

with open("fichero.txt", "r+") as file:  # "r+" - Modo lectura y escritura
    content = file.read()  # Lee todo el contenido del archivo
    #file.write("\nHola Mundo")  # Escribe al final del archivo
    #print(content)
    
    file.seek(0)  # Mueve el puntero al inicio del archivo
    for line in file.readlines():  # Itera sobre las líneas del archivo
        print(line.strip())  # Imprime cada línea sin saltos de línea adicionales
        
    #file.write("\nNuevo Teclado Mecanico Apa")
    print(file.readline())        
    
file.close()

#os.remove("fichero.txt")  # Elimina el archivo




"""
.json file
"""
import json

json_file = open("fichero.json", "r+")  

json_text = {
    "name": "Juan",
    "surname": "Perez",
    "edad": 30,
    "languages": ["Python", "JavaScript", "Java"],
    "casado": False
}

json.dump(json_text, json_file, indent=2) # Escribe el diccionario en el archivo con la función json.dump()

# El argumento indent permite formatear el archivo con la cantidad de espacios especificada

json_file.seek(0)  # Mueve el puntero al inicio del archivo

for line in json_file.readlines():
    print(line.strip())


# Conversión de JSON a diccionario
json_dict = json.load(open("fichero.json"))  # Lee el contenido del archivo con la función json.load()
# Y guardamos el contenido en un diccionario
print(json_dict)
#print(type(json_dict))
#print(json_dict["languages"])

json_file.close()



"""
.csv file
"""

import csv

csv_file = open("fichero.csv", "w+")  # "r+" - Modo lectura y escritura

csv_writer = csv.writer(csv_file)
row = ["Name", "Surname", "Age", "Language"]
csv_writer.writerow(row.split(";"))  # Escribe una fila en el archivo
csv_writer.writerow(["Juan", "Perez", 30, "Python"])  # Escribe una fila en el archivo

csv_file.seek(0)  # Mueve el puntero al inicio del archivo
for line in csv_file.readlines():
    print(line.strip())

csv_file.close()



"""
.xml file
"""
import xml