class Nota:
    def __init__(self, nombreEstudiante, nota):
        self.nombreEstudiante = nombreEstudiante
        self.nota = nota

    def haAprobado(self):
        if self.nota > 5:
            print(f'El estudiante {self.nombreEstudiante} ha sacado un {self.nota}')
            return
        else:
            print(f'El estudiante {self.nombreEstudiante} ha suspendido')


ninhoAprobado= Nota('Ninho de Aprobado', 7)
ninhoAprobado.haAprobado()

ninhoSuspenso=Nota('Ninho de Suspenso', 3)
ninhoSuspenso.haAprobado()