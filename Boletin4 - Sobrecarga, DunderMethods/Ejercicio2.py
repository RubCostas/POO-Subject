class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def __str__(self):
        return f'{self.nombre} (Vida : {self.vida}, Fuerza:  {self.fuerza})'

    def __eq__(self, other):
        return self.nombre == other.nombre

    def __lt__(self, other):     # sort() usará este método
        return self.vida < other.vida

    def comparar_fuerza(self, other):
        return self.fuerza >= other.fuerza

    def __add__(self, other):
        return Personaje(self.nombre, self.vida + other.vida, self.fuerza + other.fuerza)


arquero = Personaje('Arquero', 10, 20)
tanque = Personaje('Tanque', 40, 5)
curandero = Personaje('Curandero', 10, 15)

print(arquero)
print(tanque)

print('\n¿Es el arquero más fuerte que el tanque?')
print(arquero.comparar_fuerza(tanque))

arqueroTanque = arquero + tanque
print(arqueroTanque)

lista_heroes = [arquero, tanque, curandero]


lista_heroes.sort()   # Se ordena por vida porque __lt__ compara por vida
for heroe in lista_heroes:
    print(heroe)
