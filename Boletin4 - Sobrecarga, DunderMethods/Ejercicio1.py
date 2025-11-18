from functools import singledispatchmethod   # Importamos singledispatchmethod para poder usar sobrecarga por tipo

class Libro:
    def __init__(self, titulo, autor):
        # Este es el constructor "real".
        # Siempre recibe título y autor por separado.
        # Otros tipos de entrada se convertirán a esto en el método crear().
        self.titulo = titulo
        self.autor = autor

    @singledispatchmethod     # Hacemos que este método pueda tener varias versiones según el tipo del dato recibido
    @classmethod              # Lo hacemos de clase para poder crear objetos sin tener un objeto previo
    def crear(cls, data):
        # Esta es la versión por defecto.
        # Si llega un tipo de dato que no hemos registrado, lanzamos un error.
        raise TypeError("Entrada no soportada")

    @crear.register           # Registramos una nueva versión del método crear()
    @classmethod
    def _(cls, data: str):    # Esta versión se ejecuta cuando el argumento es un str
        # Si pasamos un único string "Título - Autor"
        # lo separamos en dos partes usando split.
        titulo, autor = data.split(" - ")
        return cls(titulo, autor)

    @crear.register           # Registramos otra versión del método crear()
    @classmethod
    def _(cls, data: tuple):
        # Se asume que la tupla viene como (titulo, autor)
        titulo, autor = data
        return cls(titulo, autor)


# Ejemplo 1: crear un libro pasando una tupla
principito = Libro.crear(("Principito", "Antoine de Saint-Exupéry"))
print(principito.titulo, principito.autor)

# Ejemplo 2: crear un libro pasando un string con el formato "Título - Autor"
biblia = Libro.crear("La Biblia - Anonimo")
print(biblia.titulo, biblia.autor)
