from limite.tela_sistema import TelaSistema
from controle.controlador_jogador import ControladorJogador
from controle.controlador_jogo import ControladorJogo
# from controle.controlador_oceano import ControladorOceano


class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_jogo = ControladorJogo(self)
        # self.__controlador_oceano = ControladorOceano(self)
        self.__tela_sistema = TelaSistema()

    def inicia_cadastro(self):
        self.__controlador_jogador.cadastra_jogador()
        self.abre_opcoes()

    def inicia_login(self):
        self.__controlador_jogo.faz_login()

    def ordena_ranking(self):
        #Use o método `sort` para ordenar com base na pontuação e, em seguida, no nome.
        self.lista_jogadores.sort(key=lambda jogador: (jogador.pontuacao, jogador.nome))


    def inicializa_sistema(self):
        self.abre_opcoes()

    def abre_opcoes(self):
        lista_opcoes = {1: self.inicia_login, 
                        2: self.inicia_cadastro,
                        0: self.encerra_sistema}
        opcao_selecionada = self.__tela_sistema.mostra_opcoes()
        funcao_escolhida = lista_opcoes[opcao_selecionada]
        funcao_escolhida()

    def encerra_sistema(self):
        exit(0)
