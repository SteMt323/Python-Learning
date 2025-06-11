from Estudiante import *
import random as rm

class Gestor:
    def __init__(self):
        self.datos = []
    
    def agregar_estudiante(self, nombre: str, calificaciones: dict, cif = rm.randint(1000, 9999)):
        estudiante_registro: Estudiante = Estudiante(cif, nombre, calificaciones)
        self.datos.append(estudiante_registro)
        try:
            self.datos.append(estudiante_registro)
            print("Se ha agrefado el estudiante...")
        except Exception as ex:
            return f"Ha ocurrido un error: \n{ex}"
        
    def eliminar_estudiante(self, cif: int):
        registro = self.datos
        for i in registro:
            if cif == registro.cif:
                self.datos[i].remove()
                print(f"Se ha eliminado el estudiante: {registro.nombre}")
                return
        print(f"No se ha encontrado el estudiante con cif {cif}")
        return
    
    def calcular_promedio_por_estudiante(self):
        registro = self.datos
        total = 0
        tam = 0
        print("\nPromedio por estudiante")
        for i in registro:
            prom = [sum(registro[i].calificaciones.values())]
            prom = prom / len(registro[i].calificaciones)
            print(f"{i+1}. {registro[i].nombre}: {prom}")
            total += prom 
            tam += 1
        self.calcular_promedio_general(total, tam)
    
    def calcular_promedio_general(self, total, tam) -> str:
        return f"El promedio general es de {total / tam}"