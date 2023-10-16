# from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
from controle.controlador_sistema import ControladorSistema

class ControladorJogo:
    def __init__(self) -> None:
        self.__controlador_sistema = ControladorSistema()
        self.__tela_jogo = TelaJogo()

    def faz_login(self):
        dados_login = self.__tela_jogo.recebe_login()
        nome, senha = dados_login["recebe_nome"], dados_login["recebe_senha"]
        if self.__controlador_sistema.__controlador_jogador.estah_cadastrado(nome, senha):
            self.inicia_jogo()
        else:
            self.__tela_jogo.mostra_mensagem("Jogador não encontrado!")
            self.faz_login(self)

    def inicia_jogo(self):
        self.__tela_jogo.mostra_mensagem("Jogo iniciado!")

    def reliza_jogada(self):
        pass
