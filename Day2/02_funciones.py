### Funciones ###

def my_function(name):
    print(f"Hello {name}")
    
my_function(input("Como te llamas?\n"))

def sum_values(x,y):
    return int(x + y)


x = int(input("Primer num:"))
y = int(input("Segundo num:"))
print(sum_values(x, y))
      
def print_texts(*texts): # De esta manera puedes pasar n parametros a la función 
    for text in texts:
        print(text.upper())
    
print_texts("Hello", "Hola", "Bonjorno", "Ohayo")