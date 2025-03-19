### Strings ###

my_string = "Hello world"

print(len(my_string)) # Medir los caracteres del string

print("Hola amigos\n" + str(5)) # "\n" salto de línea
print("Hola \t amigos") # "\t" tabulación 
print("\n")

# Formateo de strings
name, surname = "Steven", "Mejia"
age = 18

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Concatenación de cadenas y variables mediante el método "format()"
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Para concatenación de cadenas y variables mediante tipo de datos 

"""
%s: Representa una cadena de texto (str).
%d: Representa un número entero (entero con signo, int).
%f: Representa un número de punto flotante (float), con una precisión predeterminada de 6 decimales.
%x: Representa un número entero en formato hexadecimal (letras minúsculas).
%X: Representa un número entero en formato hexadecimal (letras mayúsculas).
%o: Representa un número entero en formato octal.
%e: Representa un número en notación científica (con notación "e").
%g: Utiliza una representación compacta de un número, ya sea en formato de punto flotante o notación científica, dependiendo de la magnitud.
"""
#Inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de carácteres
language = "python"
a, b, c, d, e, f = language # Cada variable con el valor language, se le asigna un caracter correspondiente
print(a) 
print(b) 

# División
print(language[1:3]) # Corte de caracteres

# Reverse
print(language[::-1]) # Invertir el orden de los caracteres

# Métodos / Funciones
print(language.lower()) # Convertir a minúsculas
print(language.upper()) # Convertir a mayúsculas
print(language.capitalize()) # Convertir la primera letra a mayúscula y el resto a min
print(language.count("t"))# Para contar los caracteres especificados
print(language.isnumeric())# Para determinar si la variable es numerica
print(language.isalpha()) # Para determinar si la variable es alfanumerica

