"""
Se implementaran las operaciones básicas de los grafos aplicado sobre listas adyacentes.
lista adyacente visualmente:
grafo = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
}
"""
class Grafo:
    def __init__(self):
        self.grafo = {}
        
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
        else:
            print(f"El vertice {vertice} ya existe....")
            return
        
    """
    Existen dos tipos de aristas, los direccionales y los no direccionales
    Direccionales:
        Son aquellos que, podríamos decirlos lineales, solo tienen una dirección no tienen una vuelta, solo una ida.
    
    No direccionales:
        Son aquellos que tienen ambas direcciones, si A apunta a B, automáticamente B apunta a A
    """    

    def agregar_arista_no_direccional(self, origen, destino):
        if origen in self.grafo[destino] or destino in self.grafo[origen]:
            print("Ya habia conexiones entre los vertices...")
            return
        elif origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append(destino)
            self.grafo[destino].append(origen)
            return
        else:
            print("Faltan vertices...")
            return
        
    def agregar_arista_direccional(self, origen, destino):
        if origen in self.grafo[destino] or destino in self.grafo[origen]:
            print("Ya habia conexiones entre los vertices...")
            return
        elif origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append(destino)
            return
        else:
            print("Faltan vertices...")
            return 
    
    def eliminar_aristas(self, origen, destino):
        if origen in self.grafo and destino in self.grafo:
            if origen in self.grafo[destino]:
                self.grafo[destino].remove(origen)
            if destino in self.grafo[origen]:
                self.grafo[origen].remove(destino)
        else:
            print("Faltan vertices...")
            
    def mostrar_conexiones(self):
        for vertice in self.grafo:
            print(f"{vertice} --> {self.grafo[vertice]}")
            
    def evaluar_conexiones(self, origen, destino) -> bool:
        if origen in self.grafo:
            return destino in self.grafo[origen]
        return False
    
def menu():
    grafo: Grafo = Grafo()
    while True:
        print("\n\n1. Agregar Vértices...")
        print("2. Agregar Aristas...")
        print("3. Eliminar Aristas...")
        print("4. Mostrar Conexiones...")
        print("5. Evaluar las conexiones....")
        print("6. Salir...")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1":
                vertice = input("Ingrese el dato: ")
                grafo.agregar_vertice(vertice)
            case "2":
                origen = input("Ingrese el vertice origen del arista: ")
                destino = input("Ingrese el vertice destino del arista: ")
                grafo.agregar_arista(origen, destino)
            case "3":
                origen = input("Ingrese el vertice origen a eliminar: ")
                destino = input("Ingrese el vertice destino a eliminar: ")
                grafo.eliminar_arista(origen, destino)
            case "4":
                grafo.mostrar_conexiones()
            case "5":
                origen = input("Ingrese el vertice origen a evaluar: ")
                destino = input("Ingrese el vertice destino a evaluar: ")
                print(grafo.conexion(origen, destino))
            case "6":
                print("Saliendo...")
                break
            case _: print("Opcion invalida, ingrese denuevo...")
    
def main():
    menu()

if __name__ == "__main__":
    main()