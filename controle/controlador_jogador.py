from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__jogadores = []
        self.__tela_jogador = TelaJogador()
        #self.__controlador_sistema = controlador_sistema



    def cadastra_jogador(self):
        dados_jogador = self.__tela_jogador.recebe_cadastro()
        jogador = Jogador(dados_jogador["nome"], dados_jogador["data_nascimento"], dados_jogador["senha"])
        self.__jogadores.append(jogador)
        self.__tela_jogador.mostra_mensagem("Cadastro realizado com sucesso!")


    def altera_cadastro(self):
        pass

    def remove_jogador(self):
        pass

    def adiciona_jogador_ranking(self):
        pass

    def lista_jogadores(self):
        for jogador in self.__jogadores:
            pass

    def encontra_cadastro(self, usuario, senha):
        for jogador in self.__jogadores:
            if jogador.usuario == usuario and jogador.senha == senha:
                return jogador
        return None

