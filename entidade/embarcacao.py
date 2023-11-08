from abc import ABC, abstractmethod

class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, tamanho: int, nome: str, posicoes: int):
        self.__tamanho = tamanho
        self.__nome = nome
        self.__posicoes = posicoes
        
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def posicoes(self):
        return self.__posicoes
    
    @tamanho.setter
    def tamanho(self, tamanho: int):
        self.__tamanho = tamanho
        
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @posicoes.setter
    def posicoes(self, posicoes: int):
        self.__posicoes = posicoes