### Tipos de errores / excepciones ###

# SyntaxError
#print "Hello world" # Descomentar para error
print("Hello world")

# NameError
name = "John" # Comentar para error
print(name)

# IndexError
my_list = [1, 2, 3, 4, 5]
#print(my_list[5]) # Descomentar para error
print(my_list[2])

# KeyError
my_dict = {"name": "John", "age": 30}
#print(my_dict["job"]) # Descomentar para error
print(my_dict["name"])

# ModuleNotFoundError
#import maths # Descomentar para error
import math

# AttributeError
#print(math.PI) # Descomentar para error
print(math.pi)

# TypeError
#result = "2" + 2 # Descomentar para error
result = "2" + "2"
print(result)

# ValueError
#number = int("hello") # Descomentar para error
number = int("123")
print(number)

# ZeroDivisionError
#result = 10 / 0 # Descomentar para error
result = 10 / 2
print(result)

# ImportError
#from math import square_root # Descomentar para error
from math import sqrt
print(sqrt(16))

# IndentationError
#def my_function(): # Descomentar para error
#    print("Hello")
#      print("World") # Mal indentado
def my_function():
    print("Hello")
    print("World")
my_function()

# FileNotFoundError
#with open("non_existent_file.txt", "r") as file: # Descomentar para error
#    content = file.read()
with open("existent_file.txt", "w") as file:
    file.write("This is a test file.")