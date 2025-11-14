"""
Diseña una clase Estudiante con los atributos nombre y nota_final. Implementa
ahora dos métodos para que los objetos de tipo Estudiante puedan compararse
directamente en función de la nota final (mayor que o menor que). Crea una lista de
estudiantes con diferentes notas y utiliza sort() para ordenarlos automáticamente de
menor a mayor.
"""
class Estudiante:
    def __init__(self, nombre, nota_final):
        self.nombre = nombre
        self.nota_final = nota_final

    def __lt__(self, other):
        print("*"*4)
        print(f'Menor que:\n')
        if self.nota_final < other.nota_final:
            print(f'{self.nombre} tiene menos nota que {other.nombre}')
            return True
        else:
            print(f'{other.nombre} tiene menos nota que {self.nombre}')
            return False
        # Mayor que (>)

    def __gt__(self, other):
        print("*" * 4)
        print(f'Mayor que:\n')
        if self.nota_final > other.nota_final:
            print(f'{self.nombre} tiene mas nota que {other.nombre}')
            return True
        else:
            print(f'{other.nombre} tiene mas nota que {self.nombre}')
            return False

estudiantes = [
    Estudiante('Estudiante1', 5),
    Estudiante('Estudiante2', 6),
]

estudiantes.sort()

print(f'*** Comparaciones ***\n')
print(estudiantes[0] < estudiantes[1])   # llama a __lt__
print(estudiantes[0] > estudiantes[1])   # llama a __gt__