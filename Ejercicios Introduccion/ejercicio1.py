class Galleta:
    def __init__(self, nombre, forma):
        self.nombre = nombre
        self.forma = forma

    def horneado(self):
        print(f'La {self.nombre}  en forma {self.forma} ha sido horneada. ¡Buen provecho!')

galleta= Galleta("galleta de avena con chocolate", "estrella")
galleta.horneado()