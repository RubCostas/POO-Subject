## Ejercicio 3
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
    
    def varia_altura(self, variacion):
        self._distancia += variacion
        return self._distancia
    
    def en_orbita(self):
        return self._distancia >= 160
    
    def varia_posicion(self, variacion_meridiano, variacion_paralelo):
        self._meridiano = self._meridiano + variacion_meridiano
        self._paralelo = self._paralelo + variacion_paralelo
        #return self._meridiano, self._paralelo
    
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