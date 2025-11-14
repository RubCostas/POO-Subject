class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = 20
    def __eq__(self, other):
        if self.nombre == other.nombre and self.edad == other.edad:
            return f'Son la misma persona'
        else: return f'No son iguales {self.nombre} y {other.nombre} '

persona1 = Persona('Alfonso', 20)
persona2 = Persona('Rubén', 20)
persona3 = Persona('Rubén', 20)
print(persona1 == persona2)
print(persona2 == persona3)
