### Anagramas ###
"""
Escribe una función que reciba dos palabras (String) y retorne 
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- No hacen falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagramas.
"""
def anagrama(word1, word2):
    # Convertimos las palabras a minusculas y eliminamos los espacios si es que los hay
    word1 = word1.lower().replace(" ","")
    word2 = word2.lower().replace(" ","")
    if word1 == word2:
        return False
    elif (sorted(word1) == sorted(word2)):
        return True
    else:
        return False
        
x = input("Ingrese la primera palabra: ")
y = input("Ingrese la segunda palabra: ")
print(anagrama(x, y))