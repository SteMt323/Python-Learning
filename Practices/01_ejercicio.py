"""
En una empresa, el rendimiento de los empleados se mide 
con una puntuación del 1 al 10. Dependiendo de la 
puntuación, el empleado recibe una clasificación. 
La clasificación se asigna de la siguiente manera:

De 1 a 3: Bajo
De 4 a 6: Medio
De 7 a 10: Alto

Escribe un programa que reciba la puntuación de varios 
empleados (puede ser una lista de puntuaciones) y 
devuelva un diccionario donde las claves son las 
clasificaciones ("Bajo", "Medio", "Alto") y los 
valores son las listas de empleados correspondientes 
a cada clasificación.
"""

def clasificar_empleados():
    # Diccionario para almacenar las clasificaciones
    resumen = {
        "Bajo": [],
        "Medio": [],
        "Alto": []
    }
    
    num_empleados = int(input("Ingrese el número de empleados a clasificar: "))
    
    for i in range(num_empleados):
        empleado = input(f"Escriba el nombre del empleado {i+1}: ")
        puntaje = int(input(f"Escriba la puntuación del empleado {i+1}: "))

        if puntaje >= 1 and puntaje <= 3:
            clasificacion = "Bajo"
        elif puntaje >= 4 and puntaje <= 6:
            clasificacion = "Medio"
        elif puntaje >= 7 and puntaje <= 10:
            clasificacion = "Alto"


        resumen[clasificacion].append(empleado)
            
    print(resumen)
    
clasificar_empleados()