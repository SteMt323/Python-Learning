class Estudiante:
    def __init__(self, cif, nombre, calificaciones: dict):
        self.cif = cif 
        self.nombre = nombre
        self.calificaciones = calificaciones
        
    def __str__(self):
        return f"Cif: {self.cif} \nEstudiante: {self.nombre}\nCalificaciones:\n".join(calificacion for calificacion in self.calificaciones.values())
        
        