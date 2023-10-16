#from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
from controle.controlador_sistema import ControladorSistema

class ControladorJogo:
    def __init__(self) -> None:
<<<<<<< Updated upstream
        pass
=======
>>>>>>> Stashed changes
        self.__controlador_sistema = ControladorSistema(self)
        self.__tela_jogo = TelaJogo()

    def faz_login(self):
        dados_login = self.__tela_jogo.recebe_login()
        nome, senha = dados_login["recebe_nome"], dados_login["recebe_senha"]
        try:
            self.__controlador_sistema.__controlador_jogador.estah_cadastrado(nome, senha)
            self.inicia_jogo()
        except:
            self.__tela_jogo.mostra_mensagem("Jogador não encontrado!")
            self.faz_login(self)

    def inicia_jogo(self):
<<<<<<< Updated upstream
        try:
            self.__tela_jogo.mostra_mensagem("Jogo iniciado!")
        except:
            self.__tela_jogo.mostra_mensagem("Jogo não iniciado!")
=======
        self.abre_opcoes()

    def inicia_partida(self):
        pass

    def voltar(self):
        pass

    def mostra_ranking(self):
        pass

    def abre_opcoes(self):
        lista_opcoes = {1: self.inicia_partida, 
                        2: self.mostra_ranking,
                        0: self.voltar}
        opcao_selecionada = self.__tela_sistema.mostra_opcoes()
        funcao_escolhida = lista_opcoes[opcao_selecionada]
        funcao_escolhida()

>>>>>>> Stashed changes

    def reliza_jogada(self):
        pass
