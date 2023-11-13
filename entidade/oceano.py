from entidade.embarcacao import Embarcacao


class Oceano:
    def __init__(self, tamanho_oceano: int, matriz, embarcacoes):
        self.__tamanho_oceano = tamanho_oceano
        self.__matriz = matriz
        self.__embarbacacoes = embarcacoes

    @property
    def embarcacoes(self):
        return self.__embarbacacoes
    
    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano
    
    @property
    def matriz(self):
        return self.__matriz
        