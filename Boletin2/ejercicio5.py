class Finanzas:
    def __init__(self, cambio_dolar_euro=1.36):
        self.cambio_dolar_euro = cambio_dolar_euro

    def dolares_euros(self, dolares):
        return dolares * self.cambio_dolar_euro

    def euros_dolares(self, euros):
        return euros / self.cambio_dolar_euro

finanzas = Finanzas()

print("100 dólares en euros:", finanzas.dolares_euros(100))
print("136 euros en dólares:", finanzas.euros_dolares(136))


finanzas_personalizado = Finanzas(1.2)
print("100 dólares en euros (cambio 1.2):", finanzas_personalizado.dolares_euros(100))
print("120 euros en dólares (cambio 1.2):", finanzas_personalizado.euros_dolares(120))
