class Persona():
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero= genero

    def presentarse(self):
        print(f'Hola soy {self.nombre}. Tengo {self.edad} y soy {self.genero}')

    def adulto(self):
        return True if self.edad >= 18 else False

persona = Persona("Ana", 25, "mujer")
persona.presentarse()

'Es adulto' if persona.adulto() else print('No es adulto')

ninho =Persona("Benjamin", 17, "hombre")
ninho.presentarse()

'Es adulto' if ninho.adulto() else print('No es adulto')