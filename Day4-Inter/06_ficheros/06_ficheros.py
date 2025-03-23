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


# .txt file

    
with open("fichero.txt", "r+") as file:  # "r+" - Modo lectura y escritura
    content = file.read()  # Lee todo el contenido del archivo
    #file.write("\nHola Mundo")  # Escribe al final del archivo
    # print(content)
    
    file.seek(0)  # Mueve el puntero al inicio del archivo
    for line in file.readlines():  # Itera sobre las líneas del archivo
        print(line.strip())  # Imprime cada línea sin saltos de línea adicionales
        
    
file.close()