import random

class Dado:
    def __init__(self):
        self.resultado = 0

    def lanzar(self):
        self.resultado = random.randint(1,6)

    def obtener(self):
        print(f'Has sacado {self.resultado}')

dado = Dado()
dado.lanzar()
dado.obtener()