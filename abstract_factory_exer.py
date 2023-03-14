# Fábrica Abstrata
class FabricaDeCarro:
    def criar_motor(self):
        pass

    def criar_bateria(self):
        pass

# Fábrica de Carros Elétricos - Filha da Fábrica Abstrata
class FabricaDeCarroEletrico(FabricaDeCarro):
    def criar_motor(self):
        return MotorEletrico()

    def criar_bateria(self):
        return BateriaLithiumIon()

# Fábrica de Carros de Gasolina - Filha da Fábrica Abstrata
class FabricaDeCarroGasolina(FabricaDeCarro):
    def criar_motor(self):
        return MotorGasolina()

    def criar_bateria(self):
        return BateriaChumboAcido()

# Produtos

# Motor Abstrato
class Motor:
    def ligar(self):
        pass

# Motor Elétrico - Filho de Motor Abstrato
class MotorEletrico(Motor):
    def ligar(self):
        print("Ligando motor elétrico...")

# Motor de Gasolina - Filho de Motor Abstrato
class MotorGasolina(Motor):
    def ligar(self):
        print("Ligando motor de gasolina...")

# Bateria Abstrata
class Bateria:
    def carregar(self):
        pass

# Bateria de Lithium-Ion - Filha de Bateria Abstrata
class BateriaLithiumIon(Bateria):
    def carregar(self):
        print("Carregando bateria lithium-ion...")

# Bateria Chumbo Ácido - Filho de Bateria Abstrata
class BateriaChumboAcido(Bateria):
    def carregar(self):
        print("Carregando bateria de chumbo ácido...")

# Código Cliente - Gera um carro a partir de uma fábrica
class Carro:
    def __init__(self, fabrica):
        self.motor = fabrica.criar_motor()
        self.bateria = fabrica.criar_bateria()

    def ligar(self):
        self.bateria.carregar()
        self.motor.ligar()

# Criando um carro elétrico
fabrica = FabricaDeCarroEletrico()
carro = Carro(fabrica)
carro.ligar()

# Criando um carro de gasolina
fabrica = FabricaDeCarroGasolina()
carro = Carro(fabrica)
carro.ligar()
