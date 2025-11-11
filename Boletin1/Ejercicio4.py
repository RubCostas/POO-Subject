## Ejercicio 4
## Implementar también con métodos estáticos

class conversor_fechas:
    
    def __init__(self, fecha=None):
        self._fecha = fecha

    def normal_americano(self):
        dia, mes, año = self._fecha.split('/')
        return f"{mes}-{dia}-{año}"
    
    def americano_normal(self):
        mes, dia, año = self._fecha.split('/')
        return f"{dia}-{mes}-{año}"
    
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha_cad):
        self._fecha = fecha_cad


conversor = conversor_fechas("01/05/2025")
print(conversor.normal_americano())
conversor.fecha = "12/30/2024"
print(conversor.americano_normal())