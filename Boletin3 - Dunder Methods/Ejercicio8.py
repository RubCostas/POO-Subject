"""
Implementa una clase Agenda que permita gestionar contactos. Los contactos deben
almacenarse internamente en un diccionario, donde las claves sean nombres de
personas y los valores, sus números de teléfono. Dentro de la clase deberán
implementarse métodos para obtener y modificar el elemento en una posición, y
otro para comprobar si un elemento se encuentra almacenado en el diccionario.
"""
class Agenda:
    def __init__(self):
        self.contactos = {
            "Persona1": 610928272,
            "Persona2": 678899772,
            "Persona3": 678894372,
            "Persona4": 678891932,
        }
    def __getitem__(self, item):
        print(f'El telefono de {item} es {self.contactos[item]}')
        return self.contactos[item]

    def __setitem__(self, index, valor):
        print(f'El telefono de {index} se ha cambiado a  {self.contactos[index]}')
        self.contactos[index] = valor
        return self.contactos[index]

    def __contains__(self, item):
        return item in self.contactos

agenda = Agenda()
agenda.__getitem__("Persona1")
agenda.__getitem__("Persona2")
agenda.__setitem__("Persona3", 000000000)
persona = agenda.__contains__("Persona8")
print(persona)

persona = agenda.__contains__("Persona3")
print(persona)
