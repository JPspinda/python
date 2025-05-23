class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, *args):
        self.modelo = args
    
class Fabricante:
    def __init__(self, marca):
        self.marca = marca
        
celta = Carro('Celta')
fusca = Carro('Fusca')
fiesta = Carro('Fiesta')
onix = Carro('Onix')
corolla = Carro('Corolla')
fusion = Carro('Fusion')

motor = Motor('1.0', '1.2', '1.4', '1.6', '1.8', '2.0')

volkswagen = Fabricante('Volkswagen')
chevrolet = Fabricante('Chevrolet')
fiat = Fabricante('Fiat')
ford = Fabricante('Ford')
toyota = Fabricante('Toyota')

corolla.motor = motor
corolla.fabricante = toyota
print()
print(f'Carro: {corolla.nome}\nMotor: {corolla.motor.modelo[4]}\nFabricante: {corolla.fabricante.marca}')

celta.motor = motor
celta.fabricante = chevrolet
print()
print(f'Carro: {celta.nome}\nMotor: {celta.motor.modelo[1]}\nFabricante: {celta.fabricante.marca}')

onix.motor = motor
onix.fabricante = chevrolet
print()
print(f'Carro: {onix.nome}\nMotor: {onix.motor.modelo[3]}\nFabricante: {onix.fabricante.marca}')

fusion.motor = motor
fusion.fabricante = chevrolet
print()
print(f'Carro: {fusion.nome}\nMotor: {fusion.motor.modelo[5]}\nFabricante: {fusion.fabricante.marca}')