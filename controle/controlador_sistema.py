from limite.tela_sistema import TelaSistema
from controle.controlador_jogador import ControladorJogador
#from controle.controlador_jogo import ControladorJogo
#from controle.controlador_oceano import ControladorOceano


class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_jogador = ControladorJogador(self)
        #self.__controlador_jogo = ControladorJogo(self)
        #self.__controlador_oceano = ControladorOceano(self)
        self.__tela_sistema = TelaSistema()

    def inicia_cadastro(self):
        self.__controlador_jogador.cadastra_jogador()
        self.abre_opcoes()

    def faz_login(self):
        pass
        

    def mostra_ranking(self):
        pass

    def inicia_jogo(self):
        pass

    def inicializa_sistema(self):
        self.abre_opcoes()

    def abre_opcoes(self):
        lista_opcoes = {1: self.faz_login, 
                        2: self.inicia_cadastro,
                        0: self.encerra_sistema}
        opcao_selecionada = self.__tela_sistema.mostra_opcoes()
        funcao_escolhida = lista_opcoes[opcao_selecionada]
        funcao_escolhida()


    def encerra_sistema(self):
        exit(0)
