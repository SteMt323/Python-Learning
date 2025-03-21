from classes import Biblioteca
import os

def menu(classes):
    opc = ""

    while True:
        print("-- Menú de la Biblioteca --")
        print("1. Agregar libros")
        print("2. Ver todos los libros")
        print("3. Ver libros disponibles")
        print("4. Ver libros prestados")
        print("5. Buscar libro por autor o titulo")
        print("6. Prestar libro")
        print("7. Devolver libro")
        print("8. Salir ")
        opc = int(input("Seleccione: "))
        
        if opc == 1:
            classes.agregar_libro()
            os.system("pause")
        elif opc == 2: 
            classes.ver_todos_libros()
            os.system("pause")
        elif opc == 3: 
            classes.ver_libros_dispo()
            os.system("pause")
        elif opc == 4: 
            classes.ver_libros_prestados()
            os.system("pause")
        elif opc == 5: 
            classes.buscar_libro_titulo_autor()
            os.system("pause")
        elif opc == 6: 
            classes.prestar_libro()
            os.system("pause")
        elif opc == 7: 
            classes.devolver_libro()
            os.system("pause")
        elif opc == 8:
            break
        else:
            print("Opción no válida")
            os.system("pause")
            
def inicializar_biblio():
    biblioteca = Biblioteca()
    return biblioteca
    