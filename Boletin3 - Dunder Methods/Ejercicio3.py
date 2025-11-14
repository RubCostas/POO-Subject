"""
Define una clase Punto que represente coordenadas bidimensionales (x e y).
Implementa un método para que dos puntos se consideren iguales únicamente si
ambas coordenadas coinciden exactamente. Posteriormente, crea una lista con
varios objetos y prueba a realizar implementaciones entre ellos.

"""
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Ejercicio 4
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            print(f'Ambos puntos son iguales, {self.x} y {self.y}')
            return self.x == other.x and self.y == other.y
        else:
            print(f'No son iguales los puntos de {self.x} y {self.y}; y {other.x} y {other.y}')
            return False

punto1=Punto(1, 2)
punto2=Punto(2, 3)
punto3=Punto(2,3)

print(punto1 == punto2)
print(punto2 == punto3)