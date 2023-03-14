# Fábrica Abstrata
class FabricaDeCarro:
    def criar_motor(self):
        pass

    def criar_bateria(self):
        pass

# Fábrica Concreta 1 - Carros Elétricos
class FabricaDeCarroEletrico(FabricaDeCarro):
    def criar_motor(self):
        return MotorEletrico()

    def criar_bateria(self):
        return BateriaLithiumIon()

# Fábrica Concreta 2 - Carros de Gasolina
class FabricaDeCarroGasolina(FabricaDeCarro):
    def criar_motor(self):
        return MotorGasolina()

    def criar_bateria(self):
        return BateriaChumboAcido()

# Produto Abstrato 1 - Motor
class Motor:
    def ligar(self):
        pass

# Produto Concreto 1.1 - Motor Elétrico
class MotorEletrico(Motor):
    def ligar(self):
        print("Ligando motor elétrico...")

# Produto Concreto 1.2 - Motor de Gasolina
class MotorGasolina(Motor):
    def ligar(self):
        print("Ligando motor de gasolina...")

# Produto Abstrato 2 - Bateria
class Bateria:
    def carregar(self):
        pass

# Produto Concreto 2.1 - Bateria Lithium-Ion
class BateriaLithiumIon(Bateria):
    def carregar(self):
        print("Carregando bateria lithium-ion...")

# Produto Concreto 2.2 - Bateria Chumbo Ácido
class BateriaChumboAcido(Bateria):
    def carregar(self):
        print("Carregando bateria de chumbo ácido...")

# Código Cliente
class Carro:
    def __init__(self, fabrica):
        self.motor = fabrica.criar_motor()
        self.bateria = fabrica.criar_bateria()

    def ligar(self):
        self.bateria.carregar()
        self.motor.ligar()

# Criar um carro elétrico
fabrica = FabricaDeCarroEletrico()
carro = Carro(fabrica)
carro.ligar()

# Criar um carro de gasolina
fabrica = FabricaDeCarroGasolina()
carro = Carro(fabrica)
carro.ligar()
