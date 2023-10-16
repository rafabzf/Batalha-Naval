#from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
import controle.controlador_sistema as controlador_sistema

class ControladorJogo:
    def __init__(self) -> None:
        self.__controlador_sistema = controlador_sistema.ControladorSistema
        self.__tela_jogo = TelaJogo

    def faz_login(self):
        '''dados_login = self.__tela_jogo().recebe_login()
        recebe_nome, recebe_senha = dados_login["recebe_nome"], dados_login["recebe_senha"]
        if self.__controlador_sistema().retorna_controlador_jogador().estah_cadastrado(recebe_nome, recebe_senha):
            self.inicia_jogo()'''
        '''else:
            self.__tela_jogo().mostra_mensagem("Jogador não encontrado!")
            self.faz_login()'''
        self.inicia_jogo()

    def inicia_jogo(self):
        self.abre_opcoes()

    def voltar(self):
        self.faz_login()


    def abre_opcoes(self):
        lista_opcoes = {1: self.inicia_partida, 
                        2: self.mostra_ranking,
                        0: self.voltar}
        opcao_selecionada = self.__tela_jogo().mostra_opcoes()
        funcao_escolhida = lista_opcoes[opcao_selecionada]
        funcao_escolhida()

    def inicia_partida(self):
        self.__tela_jogo().mostra_mensagem("Partida iniciada!")
        self.__controlador_sistema().retorna_controlador_oceano().cria_oceano()
        self.__controlador_sistema().retorna_controlador_oceano().cria_oceano_computador()


    def mostra_ranking(self):
        pass


    def realiza_jogada(self):
        pass
