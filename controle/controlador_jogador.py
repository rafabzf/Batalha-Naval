from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador


class ControladorJogador:
    def __init__(self):
        self.__jogadores = []
        self.__tela_jogador = TelaJogador()

    def cadastra_jogador(self):
        dados_cadastro = self.__tela_jogador.recebe_cadastro()
        jogador = Jogador(
            dados_cadastro["nome"], dados_cadastro["data_nascimento"], dados_cadastro["senha"])
        self.__jogadores.append(jogador)
        self.__tela_jogador.mostra_mensagem("\nCadastro realizado com sucesso!")
        self.__tela_jogador.mostra_mensagem("Faça Login para jogar! \n")

    def altera_cadastro(self):
        pass

    def remove_jogador(self):
        pass

    def adiciona_jogador_ranking(self):
        pass

    def lista_jogadores(self):
        for jogador in self.__jogadores:
            self.__tela_jogador.mostra_mensagem({"nome": jogador.nome})

    def estah_cadastrado(self, nome, senha):
        for jogador in self.__jogadores:
            if jogador.nome == nome and jogador.senha == senha:
                return True
            else:
                return False