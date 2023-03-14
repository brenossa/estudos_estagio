# Pizza base
class Pizza:
    # Define os atributos da pizza
    def __init__(self, tamanho, crosta, adicionais):
        self._tamanho = tamanho
        self._crosta = crosta
        self._adicionais = adicionais
    
    # String que deve ser retornada após a construção da pizza
    def __str__(self):
        return f"Pizza de tamanho {self._tamanho} e crosta {self._crosta} com os seguintes adicionais: {', '.join(self._adicionais)}"

# Construtor de Pizza: Constrói uma pizza do zero com os atributos selecionados pelo cliente
class ConstrutorDePizza:
    # Inicia definindo as variáveis vazias
    def __init__(self):
        self._tamanho = None
        self._crosta = None
        self._adicionais = []
    
    # Função para definir o tamanho da pizza
    def define_tamanho(self, tamanho):
        self._tamanho = tamanho
    
    # Função para definir a crosta da pizza
    def define_crosta(self, crosta):
        self._crosta = crosta

    # Função para criar um novo adicional a pizza
    def novo_adicional(self, adicional):
        self._adicionais.append(adicional)
    
    # Função para Construir a pizza com todas as variáveis definidas
    def construir(self):
        return Pizza(self._tamanho, self._crosta, self._adicionais)

construtor = ConstrutorDePizza() # Objeto da classe construtora
construtor.define_tamanho("larga")
construtor.define_crosta("grossa")
construtor.novo_adicional("carne seca")
construtor.novo_adicional("mussarela")
construtor.novo_adicional("molho de tomate")
pizza = construtor.construir() # Objeto Pizza gerado da classe construtora
print(pizza)
