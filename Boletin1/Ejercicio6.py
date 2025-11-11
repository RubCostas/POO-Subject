class Producto:
    def __init__(self, nombre, precio, cantidadDisponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible

    def actualizarPrecio(self, precio):
        self.precio = precio
        print(f"Se asigno el precio al producto \"{self.nombre}\n: {precio}")
    def aplicarDescuento(self, descuento):
        self.descuento = descuento
        precio=self.precio*(1-descuento/100)
        self.actualizarPrecio(precio)
        print(f"Se ha aplicado el descuento de {self.descuento} a su producto.")

    def actualizarCantidad(self, cantidad):
        self.cantidadDisponible = self.cantidadDisponible + cantidad
        print(f"Se ha actualizado a {self.cantidadDisponible} cantidades el producto {self.nombre} ")

    def mostrarInformacion(self):
        print(f"Tenemos {self.cantidadDisponible} del producto {self.nombre} a {self.precio} ")


ambipur = Producto("Ambipur", 1.2, 30)

ambipur.mostrarInformacion()

ambipur.actualizarCantidad(70)

ambipur.aplicarDescuento(15)
ambipur.mostrarInformacion()