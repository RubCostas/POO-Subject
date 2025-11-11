class Cuenta():
    _contador_cuenta=0000

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        self.numero_cuenta = f'C-{Cuenta._contador_cuenta}'
        Cuenta._contador_cuenta += 1

    def cantidad(self, cantidad):
        self.cantidad = cantidad
    def titular(self,titular):
        self.titular = titular
    def numero_cuenta(self,numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def ingresar(self, cantidadIngresada):
        if cantidadIngresada<0:
            print(f'No se puede ingresar una cantidad negativa')

        self.cantidad += cantidadIngresada
        print(f'Has ingresado {cantidadIngresada}. Ahora tienes {self.cantidad}')
        return self.cantidad

    def retirar(self, cantidadRetirada):
        if cantidadRetirada<0:
            print(f'No se puede retirar una cantidad negativa')

        self.cantidad -= cantidadRetirada
        print(f'Has retirado {cantidadRetirada}. Ahora tienes {self.cantidad}')
        return self.cantidad

    def mostrar_informacion(self):
        print(f"--- Información de la cuenta ---")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: {self.cantidad:.2f} €")
        print(f'Cuentas asociadas : {len(Cuenta.lista_cuentas)}')
        print("-------------------------------")


cuenta= Cuenta('Rubén', 100)

cuenta.ingresar(100)
cuenta.retirar(100)
cuenta2=Cuenta("Ramon", 500)
cuenta2.ingresar(500)
cuenta2.retirar(300)

cuenta.mostrar_informacion()