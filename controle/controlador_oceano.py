from limite.tela_embarcacao import TelaEmbarcacao
from limite.tela_oceano import TelaOceano
from entidade.oceano import Oceano
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from entidade.bote import Bote
from entidade.submarino import Submarino

class ControladorOceano:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__tela_oceano = TelaOceano()
        self.__embarcacoes = [
            PortaAvioes(7),
            Fragata(10),
            Submarino(4),
            Bote(20)
        ]
    

    
    def recebe_tamanho_oceano(self):
        tamanho = self.__tela_oceano.recebe_tamanho()
        return tamanho
        

    def cria_oceano(self, tamanho):
        matriz = [["~" for _ in range(tamanho)] for _ in range(tamanho)]
        oceano = Oceano(tamanho, matriz, self.__embarcacoes)
        return oceano  
        