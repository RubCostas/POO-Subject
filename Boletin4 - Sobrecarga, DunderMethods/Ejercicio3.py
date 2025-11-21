from functools import singledispatchmethod


class Dinero:
    def __init__(self, cantidad: int, divisa = None):
        self.cantidad = cantidad
        self.divisa = divisa


    @singledispatchmethod
    @classmethod
    def crear(cls, data):
        raise TypeError("Entrada no soportada")

    @__init__.register
    @classmethod
    def _(cls, cantidad: int):
        return cls(cantidad,"€")


    @__init__.register
    @classmethod
    def _(cls, data: str):
        cantidad, divisa = data.split(" ")
        return cls(cantidad, divisa)

    def __str__(self):
        return f"{self.cantidad} {self.divisa}"

yenes = Dinero(5.05,"JPY")
print(yenes)

euros =Dinero("20 Yenes")
print(euros)