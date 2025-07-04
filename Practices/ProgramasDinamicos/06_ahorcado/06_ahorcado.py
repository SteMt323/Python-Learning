"""
💬 2. Ahorcado clásico
La máquina elige una palabra secreta.

Tú tienes que adivinarla letra por letra.

Tienes 6 intentos antes de que el monito ahorcado muera 😵

Cada error te acerca más al final.

💡 Puedes mostrar el progreso con algo como _ _ e _ _ _ y usar listas para mostrar qué letras ya usaste.
"""
from palabras import Palabras
import random as rd

class Ahorcado:
    def __init__(self):
        pass
    
    def category_selection(self) -> int:
        pl = Palabras()
        for i, category in enumerate(pl.categorias.keys()):
            print(f"{i+1}. {category}")
        while True:
            category = input("Seleccione una de las categorias (1-6): ")
            if category.isdigit():
                category = int(category)
                if category in range(1, 7):
                    break
                else: print("Opcion invalida...") 
            else: print("Opcion invalida...")
        return category
    
    def start(self):
        ahorcado = Ahorcado()
        pl = Palabras()
        selection = self.category_selection()
        category = list(pl.categorias)[selection-1]
        keyword = rd.choice(list(pl.categorias[category]))
        print(keyword)
        print(f"Se ha seleccionado la Categoría: {category}")
        attemps = 0
        while True:
            if attemps == 6:
                print("Has perdido...")
                break
            
            
            
    
    def print_progress(self, keyword, playerword):
        pass

a = Ahorcado()
a.start()
