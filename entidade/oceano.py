from entidade.embarcacao import Embarcacao

class Oceano:
    def __init__(self, tamanho_oceano: int, embarcacoes: [Embarcacao]):
        self.__tamanho_oceano = tamanho_oceano
        self.__embarcacoes = embarcacoes

    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano
    
    @tamanho_oceano.setter
    def tamanho_oceano(self, tamanho_oceano):
        self.__tamanho_oceano = tamanho_oceano
    

        
    def embarcacoes(self):
        return self.__embarcacoes
    
    def adiciona_embarcacao(self, embarcacao: Embarcacao):
        self.__embarcacoes.append(embarcacao)
        