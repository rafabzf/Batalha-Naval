from embarcacao import Embarcao


class Fragata(Embarcao):
    def __init__(self, tamanho: int, nome: str, posicoes: int, num_canhoes: int):
        super().__init__(tamanho, nome, posicoes)
        self.__num_canhoes = num_canhoes
        
    @property
    def num_canhoes(self):
        return self.__num_canhoes
    
    @num_canhoes.setter
    def num_canhoes(self, num_canhoes):
        self.__num_canhoes = num_canhoes