from abc import ABC, abstractmethod

class Embarcacao(ABC):
    @abstractmethod
    def __init__(self, nome, sigla, tamanho, quantidade):
        self.nome = nome
        self.sigla = sigla
        self.quantidade = quantidade
        self.tamanho = tamanho  

        
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def nome(self):
        return self.__nome

    @tamanho.setter
    def tamanho(self, tamanho: int):
        self.__tamanho = tamanho
        
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
