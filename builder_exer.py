class Pizza:
    def __init__(self, tamanho, crosta, adicionais):
        self._tamanho = tamanho
        self._crosta = crosta
        self._adicionais = adicionais
    
    def __str__(self):
        return f"Pizza de tamanho {self._tamanho} e crosta {self._crosta} com os seguintes adicionais: {', '.join(self._adicionais)}"

class ConstrutorDePizza:
    def __init__(self):
        self._tamanho = None
        self._crosta = None
        self._adicionais = []
    
    def define_tamanho(self, tamanho):
        self._tamanho = tamanho
    
    def define_crosta(self, crosta):
        self._crosta = crosta

    def novo_adicional(self, adicional):
        self._adicionais.append(adicional)
    
    def construir(self):
        return Pizza(self._tamanho, self._crosta, self._adicionais)

construtor = ConstrutorDePizza()
construtor.define_tamanho("larga")
construtor.define_crosta("grossa")
construtor.novo_adicional("carne seca")
construtor.novo_adicional("mussarela")
construtor.novo_adicional("molho de tomate")
pizza = construtor.construir()
print(pizza)
