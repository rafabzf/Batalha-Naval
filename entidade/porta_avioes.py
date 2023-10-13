from entidade.embarcacao import Embarcao

class PortaAvioes(Embarcao):
    def __init__(self, tamanho: int, nome: str, posicoes: int, num_avioes: int):
        super().__init__(tamanho, nome, posicoes)
        self.__num_avioes = num_avioes
        
    @property
    def num_avioes(self):
        return self.__num_avioes
    
    @num_avioes.setter
    def num_avioes(self, num_avioes):
        self.__num_avioes = num_avioes
        