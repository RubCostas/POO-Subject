from time import sleep

# Variable global del consumo total
consumo_total = 0

class Aparato:
    def __init__(self, consumo):
        self.consumo = consumo
        self.encendido = False

    def encender(self):
        """
        Enciende el aparato e incrementa el consumo total.
        """
        global consumo_total
        if not self.encendido:
            self.encendido = True
            consumo_total += self.consumo
            print("Aparato encendido.")
            print(f"Consumo total: {consumo_total}")
        else:
            print("El aparato ya está encendido.")

    def apagar(self):
        """
        Apaga el aparato y disminuye el consumo total hasta 0 si corresponde.
        """
        global consumo_total
        if self.encendido:
            print("Iniciando apagado...")
            self.encendido = False

            # Simulamos el descenso gradual del consumo
            while consumo_total > 0 and consumo_total - self.consumo >= 0:
                consumo_total -= self.consumo
                print(f"Consumo bajando... {consumo_total}")
                sleep(1)

            # Evitar que quede negativo por redondeos
            if consumo_total < 0:
                consumo_total = 0

            print("Aparato apagado completamente.")
            print(f"Consumo total final: {consumo_total}")
        else:
            print("El aparato ya estaba apagado.")


tostadora = Aparato(10)
televisor=Aparato(20)
# Encendemos y simulamos funcionamiento durante un tiempo
tostadora.encender()
televisor.encender()

for _ in range(5):
    print(f"Consumo total: {consumo_total}")
    sleep(3)

# Apagamos el aparato
tostadora.apagar()
televisor.apagar()