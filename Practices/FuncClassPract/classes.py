
class Libro():
    def __init__(self, titulo, autor, estado):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado
        
    def estado_libro(self):
        if self.estado == True:
            return "El libro está disponible"
        if self.estado == False:
            return "El libro está prestado"
        
class Biblioteca():
    def __init__(self, libros = list()):
        self.libros = libros
        
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        est = input("¿El libro está disponible? (S/N): ")
        estado = lambda est: True if est == "S" else False
        
        self.libros = Libro(titulo, autor, estado(est))
        print("El libro se ha agregado con exito!")
        
    def ver_todos_libros(self):
        for libro in self.libros:
            print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Estado: {libro.estado}")
            
    def ver_libros_dispo(self):
        for libro in self.libros:
            if libro.estado == True:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}")
            
    def ver_libros_prestados(self):
        for libro in self.libros:
            if libro.estado == False:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}")
                
    def prestar_libro(self):
        titulo = input("Ingrese el título del libro a prestar: ")
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.estado = False
                print(f"El libro {libro.titulo} de {libro.autor} ha sido prestado")
    
    def devolver_libro(self):
        titulo = input("Ingrese el título del libro a devolver: ")
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.estado = True
                print(f"El libro {libro.titulo} de {libro.autor} ha sido prestado")
                
    def buscar_libro_titulo_autor(self):
        opc = input("Desea buscar el libro por: \n 1- Titulo \n 2- Autor \n 3- Ambos")
        if opc == "1":
            titulo = input("Ingrese el título del libro: ")
            for libro in self.libros:
                if libro.titulo == titulo:
                    print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Estado: {libro.estado}")
                    
        elif opc == "2":
            autor = input("Ingrese el autor del libro: ")
            for libro in self.libros:
                if libro.autor == autor:
                    print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Estado: {libro.estado}")

        elif opc == "3":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            for libro in self.libros:
                if libro.titulo == titulo and libro.autor == autor:
                    print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Estado: {libro.estado}")

        else: 
            print("Opción no válida")
        