class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        return print(self.numero1 + self.numero2)

    def resta(self):
        return print(self.numero1 - self.numero2)

    def multiplicacion(self):
        return print(self.numero1 * self.numero2)

    def division(self):
        if self.numero2 == 0:
            return print('No se puedo dividir por cero.')
        return print(self.numero1 / self.numero2)


operacion1 = Operacion(4, 0)
operacion1.suma()
operacion1.resta()
operacion1.multiplicacion()
operacion1.division()
