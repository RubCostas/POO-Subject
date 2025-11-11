class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrarInformacion(self):
        print(f'El libro titulado {self.titulo} del autor {self.autor} tiene un precio de venta de {self.precio} euros.')

libro = Libro("POO en Python", "Pepe Pérez", 15)

libro.mostrarInformacion()