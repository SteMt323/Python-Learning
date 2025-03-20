### Clases ###

# "self" es un parámetro obligatorio en los métodos de instancia en Python y hace referencia al objeto que se está creando.

class MyPerson:
    def __init__(self, name, surname): # Inicializa el constructor de clase, se crea una nueva instancia de la clase
        self.name = name # Se le asignan los valores a los atributos de la clase
        self.surname = surname
        
    def walk (self): # Para pasarle argumentos del objeto a la función, hay que pasar por parametro "self"
        print(f"{self.name} {self.surname} esta caminando...")
        
my_person = MyPerson("Steven", "Morgan")
print(f"{my_person.name} {my_person.surname}")
my_person.walk()    