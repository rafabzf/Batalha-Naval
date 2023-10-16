# from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo

class ControladorJogo:
    def __init__(self) -> None:
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

    def realiza_jogada(self):
        pass
