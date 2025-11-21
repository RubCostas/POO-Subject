class Libro:
    def __init__(self, titulo:str, autor:str, anio:int):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f'{self.titulo} ({self.autor} - {self.anio})'

    def __repr__(self):
        return f'{self.__class__.__name__} (Título={self.titulo},  Anio={self.anio})'

    def __eq__(self, other):
        if self.titulo == other.titulo and self.autor == other.autor:
            return True
        else:
            return False

class Biblioteca:
    def __init__(self):
        self.colecciones= []

    def anhadirLibro(self, libro:Libro):
        self.colecciones.append(libro)
        return self.colecciones

    def __len__(self):
        return len(self.colecciones)

    def __getitem__(self, item):
        return self.colecciones[item]

    def __setitem__(self, item, valor: Libro):
        self.colecciones.__setitem__(item, valor)

    def __contains__(self, item):
        return item in self.colecciones

    def __repr__(self):
        return f'{self.colecciones})'


principito = Libro("El principito", "Antoine", "1976")
principazo = Libro("El principazo", "Antoine", "1976")
libro1 =Libro("El libro 1", "Anonimo", "2000")
libro2 = Libro("El libro 2", "Anonimo", "2000")
libro3 = Libro("El libro 3", "Anonimo", "2000")
print(f'\nSTR del libro\n')
print(principito)

print(f'\nComparacion de libros\n')
print(principazo==principito)

print(f'\nCreacion de biblioteca libros\n')
moanha = Biblioteca()
moanha.anhadirLibro(libro1)
moanha.anhadirLibro(libro2)
moanha.anhadirLibro(libro3)
print(len(moanha))

cangas = Biblioteca()
cangas =  cangas.anhadirLibro(libro3)
print(len(cangas))

print(f'\nVer los items de las colecciones\n')
print(f'\nMoaña\n')
print(moanha.__getitem__(0))
print(f'\nCangas')
print(cangas.__getitem__(0))

print(f'\nSetear un libro')
belair =Libro("El principe de BelAir", "Will Smith", "2001")

moanha.__setitem__(item=0, valor=belair)

print(moanha.__getitem__(0))

libroBuscado = "El principe de BelAir"
esta = moanha.__contains__(libroBuscado)
print(esta)

print(f'\nListado de libros')
print(moanha.__dict__)
