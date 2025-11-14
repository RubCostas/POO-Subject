class Persona:
    def __init__(self, nombre, edad, profesion):
        self._nombre = nombre
        self._edad = edad
        self.profesion = profesion

    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad

    def __str__(self):
        return f'Se llama {self.nombre}, tiene  {self.edad} y trabaja en {self.profesion}'

    def __repr__(self):
        return f'{self.__module__}, {self.__dict__}'


persona = Persona(nombre='Alfonso', edad=25, profesion='Python')
print(repr(persona))

print(str(persona))