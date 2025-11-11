from unittest.mock import PropertyMock


class Persona:
    def __init__(self, nombre, edad=None):
        self.nombre = nombre
        self._edad = edad if edad is not None else 0

    @property
    def edad(self):
        return self._edad


    def presentarse(self):
        print(f"Soy {self.nombre} y tengo  {self._edad} años")

    @edad.setter
    def cambiarEdad(self, valor):
        if valor < 0:
            self._edad = valor
        else:
            raise ValueError("El valor debe ser mayor a 0")

        print(f"{self.nombre} ha cambiado de edad a {valor} años.")

    def __del__(self):
        print(f"{self.nombre} ha sido eliminado de la base de datos.")

julia=Persona("Julia", 24)
julia.presentarse()

marcos=Persona("Marcos")
marcos.presentarse()

#marcos.cambiarEdad(24)

perico=Persona("Perico")
perico.presentarse()

del perico