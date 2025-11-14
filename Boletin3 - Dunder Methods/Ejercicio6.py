"""
Implementa ahora dos métodos que calculen: el producto escalar si se multiplica por
otro Punto; y el escalado si se multiplica por un número.
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
    #Suma de Puntos (da objeto)
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    #Resta de Puntos (da objeto)
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Punto(self.x * other.x, self.y * other.y)
    def __rmul__(self,num):
        return Punto(self.x * num, self.y * num)
"""  Caso resuelto por Nuria
def __mul__(self, otro):
    # Caso 1: producto escalado (int o float)
    if isinstance(otro, (int, float)):
        return Punto(self.coordX * otro, self.coordY * otro)

    # Caso 2: multiplicación por otro punto (producto escalar)
    elif isinstance(otro, Punto):
        return self.coordX * otro.coordX + self.coordY * otro.coordY

    else:
        raise TypeError(f"No se puede multiplicar Punto por {type(otro)}")
        
"""






punto1=Punto(1, 2)
punto2=Punto(2, 3)
punto3=Punto(2,3)

print(punto1 == punto2)
print(punto2 == punto3)

punto4=punto1 + punto2 #3, 5
print(f'El nuevo punto sumando es {punto4.__dict__}')

punto5=punto1-punto2
print(f'El nuevo punto restando es {punto5.__dict__}')


producto_escalar=punto1.__mul__(punto2)
print(f'El nuevo producto es {producto_escalar.__dict__}')

producto_escalado=punto1.__rmul__(4)
print(f'El nuevo producto es {producto_escalado.__dict__}') #1,2 * 4 = 4 y 8