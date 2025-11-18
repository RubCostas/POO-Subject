from operator import concat


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def __str__(self):
        return f'{self.nombre} ({self.precio}€ x {self.cantidad} unidades)'

    def __eq__(self, other):
        return self.nombre == other.nombre

    def precio_total(self):
        return self.precio * self.cantidad

class Carrito:
    def __init__(self, productos=None):
        self.productos_lista = productos if productos is not None else []

    def __add__(self, other):
        return Carrito(self.productos_lista + other.productos_lista)

    def __len__(self):
        return len(self.productos_lista)

    def anhadir_carrito(self,Producto):
        self.productos_lista.append(Producto)
        return self.productos_lista

    def __getitem__(self, item):
        return self.productos_lista[item]

    def __str__(self):
        return ", ".join(map(str, self.productos_lista))

print(f'\nProductos de Tienda:')
camisetas = Producto('Camiseta', 10, 20)
tenedores = Producto('Tenedores', 2, 30)
altavoces = Producto('Altavoces', 4, 50)

print(camisetas)
print(tenedores)
print(altavoces)

print(camisetas.precio_total())
print(camisetas == tenedores)

carritoRuben = Carrito([camisetas,camisetas, tenedores])
print(len(carritoRuben))

carritoRamon = Carrito([altavoces,altavoces])

print(carritoRuben.__str__())

carritoJunto = carritoRamon + carritoRuben
print(carritoJunto.__len__())