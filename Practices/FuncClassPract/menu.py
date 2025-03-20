from classes import Biblioteca, Libro

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
        elif opc == 2: 
            classes.ver_todos_libros()
        elif opc == 3: 
            classes.ver_libros_dispo
        elif opc == 4: 
            classes.ver_libros_prestados()
        elif opc == 5: 
            classes.buscar_libro_titulo_autor()
        elif opc == 6: 
            classes.prestar_libro()
        elif opc == 7: 
            classes.devolver_libro()
        elif opc == 8:
            break
        else:
            print("Opción no válida")
            
def inicializar_biblio():
    biblioteca = Biblioteca()
    return biblioteca
    