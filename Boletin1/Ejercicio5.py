## Ejercicio 5
class estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agrega_calificacion(self, nota):
        self.calificaciones.append(nota)
    
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def mostrar_informacion(self):
        promedio = self.calcular_promedio()
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio de calificaciones: {promedio:.2f}")

est = estudiante("Ana", 20)
est.agrega_calificacion(8.5)
est.agrega_calificacion(9.0)
est.mostrar_informacion()

        