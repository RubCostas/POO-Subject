"""
Implementa ahora la resta de puntos con el operador -.
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            print(f'Ambos puntos son iguales, {self.x} y {self.y}')
            return self.x == other.x and self.y == other.y
        else:
            print(f'No son iguales los puntos de {self.x} y {self.y}; y {other.x} y {other.y}')
            return False

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)

punto1=Punto(1, 2)
punto2=Punto(2, 3)
punto3=Punto(2,3)

print(punto1 == punto2)
print(punto2 == punto3)

punto4=punto1 + punto2 #3, 5
print(f'El nuevo punto sumando es {punto4.__dict__}')

punto5=punto1-punto2
print(f'El nuevo punto restando es {punto5.__dict__}')