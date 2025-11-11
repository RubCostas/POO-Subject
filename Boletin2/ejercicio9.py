import datetime as dt

class Cuenta():
    _contador_cuenta=0
    lista_cuentas=[]

    def __init__(self, titular, cantidad=None):
        self._titular = titular
        self._cantidad = cantidad
        self._numero_cuenta = f'C-{Cuenta._contador_cuenta}'
        Cuenta._contador_cuenta += 1
        Cuenta.lista_cuentas.append(self)

    @property
    def cantidad(self):
        return self._cantidad
    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

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
        print(f"\n--- Información de la cuenta ---")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo actual: {self.cantidad:.2f} €")
        print(f'Cuentas asociadas : {len(Cuenta.lista_cuentas)}')
        print(self._titular.mostrar_informacion())
        print("-------------------------------")




class Titular():
    def __init__(self, nombre="Pepe", fecha_nacimiento="2009-05-20", dni="99999999D", sexo="H",direccion="Moncloa"):
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.dni=dni
        self.sexo=sexo
        self.direccion=direccion

    def es_mayor_de_edad(self):
        fecha_nacimiento= dt.datetime.strptime(self.fecha_nacimiento,'%Y-%m-%d').date()
        hoy= dt.date.today()
        diferencia= hoy.year-fecha_nacimiento.year
        if diferencia>18:
            return True
        else:
            return False

    def comprobar_sexo(self, sexoIntroducido):
        if self.sexo==sexoIntroducido:
            print(f'Los datos son correctos. [{sexoIntroducido}]')
            return True
        else:
            self.sexo="H"
            print("Se ha asignado el género H")
            return False

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}\n'
              f'Fecha Nacimiento: {self.fecha_nacimiento}\n'
              f'Es mayor de edad:{self.es_mayor_de_edad()}\n'
              f'DNI: {self.dni}\n'
              f'Sexo: {self.sexo}\n'
              f'Direccion: {self.direccion}\n')



ruben = Titular(nombre="Rubén", fecha_nacimiento="1990-03-15", dni="12345678A", sexo="H", direccion="Madrid")
cuenta= Cuenta(ruben, 100)

cuenta.ingresar(100)
cuenta.retirar(100)
cuenta2=Cuenta("Ramon", 500)
cuenta2.ingresar(500)
cuenta2.retirar(300)



ruben.comprobar_sexo("H")
ruben.comprobar_sexo("M")
cuenta.mostrar_informacion()