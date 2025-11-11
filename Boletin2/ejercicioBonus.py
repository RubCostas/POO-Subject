class Departamento:
    def __init__(self, codigo,nombre, localizacion):
        self._codigo = codigo
        self._nombre = nombre
        self._localizacion = localizacion
    def mostrarInformaciónDepartamento(self):
        return(f'Codigo: {self.codigo}\n'
              f'Nombre: {self.nombre}\n'
              f'Localizacion: {self.localizacion}\n')

    @property
    def codigo(self):
        return self._codigo
    @property
    def nombre(self):
        return self._nombre
    @property
    def localizacion(self):
        return self._localizacion


class Empleado:
    def __init__(self, nombre, funcion, salario, numero_horas,departamento):
        self.nombre = nombre
        self.funcion = funcion
        self._salario = salario
        self.numero_horas = numero_horas
        self.departamento = departamento

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value

    def departamento(self):
        return self.departamento

    def trabajar(self, num_horas):
        self.numero_horas = self.numero_horas + num_horas
        print(f'\nEl trabajador ha hecho {self.numero_horas} horas')
        return self.numero_horas

    def consultarSalario(self):
        salario= str(self.salario)
        print(f'El salario del trabajador es de {salario}')
        return salario

    def modificarSalario(self, value):
        self.salario = self.salario + value
        if value < 0:
            print(f'El salario del trabajador se ha reducido en {value}€: {self.salario}')
        else: print(f'El salario del trabajador se ha aumentado en {value}: {self.salario}')

    def mostrarInformación(self):
        print(f'\nInformación del empleado:\n'
              f'Nombre: {self.nombre}\n'
              f'Funcion: {self.funcion}\n'
              f'Salario: {self.salario}\n'
              f'Numero horas: {self.numero_horas}\n'
              f'Departamento: \n{self.departamento.mostrarInformaciónDepartamento()}\n')

departamentoIT = Departamento('IT','Informática','Moaña')
ruben = Empleado("Rubén", "Soporte Informático", 2000, 50,departamentoIT)

ruben.trabajar(100)
ruben.modificarSalario(200)

ruben.mostrarInformación()