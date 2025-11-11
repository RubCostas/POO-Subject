class restaurante:

    def __init__(self):
        pass

    def calcular_comensales(self, papas, chocos):
        comensales = 0
        p = papas
        c = chocos
        while p >= 1 and c >= 0.5:
            p -= 1
            c -= 0.5
            comensales += 3

        return comensales


rest = restaurante()
print(rest.calcular_comensales(3, 1.5))  # Ejemplo de uso