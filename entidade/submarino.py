from entidade.embarcacao import Embarcao


class Submarino(Embarcao):
    def __init__(self, tamanho: int, nome: str, posicoes: int, profundidade: int):
        super().__init__(tamanho, nome, posicoes)
        self.__profundidade = profundidade
        
    @property 
    def profundidade(self):
        return self.__profundidade
    
    @profundidade.setter
    def profundidade(self, profundidade):
        self.__profundidade = profundidade