from functools import singledispatchmethod


class Dinero:
    def __init__(self, cantidad, divisa = "€"):
        self.cantidad = cantidad
        self.divisa = divisa

    @singledispatchmethod
    @classmethod
    def crear(cls, data):
        raise TypeError("Entrada no soportada")

    @crear.register
    @classmethod
    def _(cls, cantidad: int):
        return cls(cantidad,"€")

    @crear.register
    @classmethod
    def _(cls, data: tuple):
        cantidad, divisa = data
        return cls(cantidad, divisa)

    def __str__(self):
        return f"{self.cantidad} {self.divisa}"

yenes = Dinero(5,"JPY")
print(yenes)

euros =Dinero(20)
print(euros)