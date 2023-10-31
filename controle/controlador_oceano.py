from limite.tela_embarcacao import TelaEmbarcacao
from limite.tela_oceano import TelaOceano

class ControladorOceano:
    def __init__(self, controlador_sistema):
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__tela_oceano = TelaOceano()
        self.__controlador_sistema = controlador_sistema
        self.__tamanho_oceano = None
    
    
    def armazena_tamanho_oceano(self):
        self.__tamanho_oceano = self.__tela_oceano.recebe_tamanho()


    def cria_oceano(self):
        oceano = [['O' for _ in range(self.__tamanho_oceano)] for _ in range(self.__tamanho_oceano)]
        return oceano
    
    def cria_oceano_computador(self):
        self.cria_oceano()
    
    def adiciona_embarcacao_oceano(self):
        pass
