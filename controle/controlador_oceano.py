from limite.tela_embarcacao import TelaEmbarcacao
from limite.tela_oceano import TelaOceano

class ControladorOceano:
    def __init__(self, controlador_sistema):
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__tela_oceano = TelaOceano()
        self.__controlador_sistema = controlador_sistema
    
    def cria_oceano(self):
        tamanho_oceano = self.__tela_oceano.recebe_tamanho()
        oceano = [['O' for _ in range(tamanho_oceano)] for _ in range(tamanho_oceano)]
        return oceano
    
    def cria_oceano_computador(self):
        tamanho_oceano = self.__tela_oceano.recebe_tamanho()
        oceano_computador = [['O' for _ in range(tamanho_oceano)] for _ in range(tamanho_oceano)]
        return oceano_computador
    
    def adiciona_embarcacao_oceano(self):
        pass
