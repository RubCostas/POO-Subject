class Consumo:
    def __init__(self, kms= 0, litros=0, vmed=0, pgas=0):
        self.kms = kms
        self.litros = litros
        self.vmed = vmed
        self.pgas = pgas

    def get_tiempo(self, kms):
        if self.kms <0:
            return 0
        else:
            tiempo = (self.kms/self.vmed)
            print(f'Tiempo de viaje: {tiempo}')
            return tiempo

    def consumo_medio(self, kms):
        if kms < 0:
            return 0

        consumo = (self.litros/kms)
        print(f'Consumo medio: {round(consumo,2)}')
        return consumo

    def consumo_euros(self):
        consumo = (self.litros /self.kms) * self.pgas
        print(f'El coche ha consumido {round(consumo,2)} en los {self.kms} recorridos ({self.pgas} €/Litro) ')
        return consumo


viaje = Consumo(kms=300, litros=100, vmed=50, pgas=10)
viaje.get_tiempo(24)
viaje.consumo_euros()
viaje.consumo_medio(50)

