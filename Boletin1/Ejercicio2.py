## Ejercicio2.py
class satelite:
    def __init__(self, meridiano=None, paralelo=None, distancia=None):
        self._meridiano = meridiano if meridiano is not None else 0.000
        self._paralelo = paralelo if paralelo is not None else 0.000
        self._distancia = distancia if distancia is not None else 0

    def set_posicion(self, meridiano, paralelo, distancia):
        self._meridiano = meridiano
        self._paralelo = paralelo
        self._distancia = distancia

    def print_posicion(self):
        return f"El satélite está orbitando en meridiano {self.meridiano}, paralelo {self.paralelo} a una distancia de la tierra de {self.distancia}km."
    
    @property
    def meridiano(self):
        return self._meridiano
    
    @property
    def paralelo(self):
        return self._paralelo
    
    @property
    def distancia(self):
        return self._distancia
    
    @meridiano.setter
    def meridiano(self, valor):
        self._meridiano = valor

    @paralelo.setter
    def paralelo(self, valor):
        self._paralelo = valor

    @distancia.setter
    def distancia(self, valor):
        self._distancia = valor


sat = satelite(50, 20, 4500)
print("Meridiano:", sat.meridiano)
sat.paralelo = 85
print("Paralelo:", sat.paralelo)
print(sat.print_posicion())