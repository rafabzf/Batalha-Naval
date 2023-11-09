from entidade.embarcacao import Embarcacao

class Bote(Embarcacao):
    def __init__(self, tamanho: int, nome: str, posicoes: int, num_coletes: int):
        super().__init__(tamanho, nome, posicoes)
        self.__num_coletes = num_coletes
        
    @property
    def num_coletes(self):
        return self.__num_coletes
    
    @num_coletes.setter
    def num_coletes(self, num_coletes):
        self.__num_coletes = num_coletes
        