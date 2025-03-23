### Cadenas invertidas ###
"""
Crea un programa que invierta el orden de una cadena de texto sin usar
las funciones propias del lenguaje que lo hagan de fora automática.
Si le pasamos un "Hola mundo", nos retornaria "odnum aloH"
"""
def invertir_cadena(cadena):
    reversed_text = ""
    for i in range(len(cadena)):
        reversed_text = cadena[i] + reversed_text
    return reversed_text
        
        
word = input("Ingrese la cadena: ")
print(invertir_cadena(word))  