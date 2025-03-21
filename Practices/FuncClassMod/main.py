from menu import inicializar_biblio, menu

"""
Practica de funciones, clases y modulos
"""

def main():
    biblioteca = inicializar_biblio()
    menu(biblioteca)
    
if __name__ == "__main__":
    main()
    