from entidade.embarcacao import Embarcacao

class Oceano:
    def __init__(self, tamanho_oceano: int, embarcacoes: [Embarcacao]):
        self.__tamanho_oceano = tamanho_oceano
        self.__embarcacoes = embarcacoes
        
    def embarcacoes(self):
        return self.__embarcacoes
    
    def adiciona_embarcacao(self, embarcacao: Embarcacao):
        self.__embarcacoes.append(embarcacao)
        