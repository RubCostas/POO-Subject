from functools import singledispatchmethod

class Figura:
    def __init__(self, radio=int, base=int, altura=int):
        self.radio = radio
        self.base = base
        self.altura = altura

    @singledispatchmethod
    @classmethod
    def crear(cls, data):
        raise TypeError("Entrada no soportada")

    @crear.register
    @classmethod
    def _(cls, radio: int):
        print(f'\nRadio del círculo: {radio}')
        return cls(radio=radio)


    @crear.register
    @classmethod
    def _(cls, datos: str):
        base, altura = datos.split(" ")
        base = int(base)
        altura = int(altura)

        if altura < 0:
            raise ValueError('Altura no válida')
        if base < 0:
            raise ValueError('Base no válida')

        print(f'\nTengo un rectángulo de base: {base} y altura: {altura}')
        return cls(base=base, altura=altura)


# Uso
circulo = Figura.crear(5)
rectangulo = Figura.crear("25 10")