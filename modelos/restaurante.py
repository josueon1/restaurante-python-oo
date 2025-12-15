from modelos.avaliacao import Avaliacao

# código omitido
class Restaurante:
    restaurantes = []  #criando uma lista para a classe restaurante

    @classmethod  # método de classe para listar os restaurantes
    def listar_restaurantes(cls):
        print('nome do restaurante'.title().ljust(20), '|', 'categoria'.title().ljust(20), '|', 'avaliaçao'.title().ljust(20) ,'|','ativo/inativo'.title())
        for restaurante in cls.restaurantes: # for para cada restaurante in na lista de Restaurante.restaurantes
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    def __init__(self,nome,categoria):# método construtor \ O método construtor __init__ não retorna nada em Python.
        self.nome = nome.upper()
        self.categoria = categoria.title() # o title() coloca a primeira letra de cada palavra em maiusculo 
        self._ativo = False
        self._avaliacao=[]
        Restaurante.restaurantes.append(self)  # adicione(append) a Restaurante à lista de restaurantes da classe

    def __str__(self):#  método para retornar uma string representando o restaurante
        return f'{self.nome} | {self.categoria}'

    def mudar_status(self):
        self._ativo = not self._ativo

    @property #  esse e o metodo decorator ele transforma um método em um atributo somente leitura
    def ativo(self):
        return '☒ ☐' if self._ativo else '☐ ☒' #esses  simbolos foi baixado do coolsymbol.com
    
 
    def receber_avaliacao(self,cliente,nota):
        avaliacao=Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if len(self._avaliacao)==0:
            return 0
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_de_notas)
        return media
        
        