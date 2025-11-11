 ## Ejercicio 1
class numero:

    def __init__(self, num=None):
        self.num = num if num is not None else 0 

    def aniade (self, valor):
        self.num += valor # self.num = self.num + valor

    def resta (self, valor):
        self.num -= valor

    def get_valor(self):
        return self.num
    
    def get_doble(self):
        return self.num * 2
    
    def get_triple(self):
        return self.num * 3
    
    def set_numero(self, num):
        self.num = num


num = numero(7)
num.aniade(3)
print(num.get_valor())
num.resta(2)
print(num.get_valor())
print(num.get_doble())
print(num.get_triple())