from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador
from controle.controlador_execessao import Controlador_excessao
import datetime


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__controlador_execessao = Controlador_excessao()
        self.__jogadores = []

    def cadastra_jogador(self):
        dados_jogador = self.__tela_jogador.recebe_cadastro()

        try:
            data_nascimento = datetime.datetime.strptime(dados_jogador["data_nascimento"], "%d/%m/%Y")
        except ValueError:
            self.__tela_jogador.mostra_mensagem("Formato de data de nascimento inválido. Tente novamente.")
            self.cadastra_jogador()
            return

        for jogador in self.__jogadores:
            if dados_jogador["nome"] == jogador.nome and data_nascimento == jogador.data_nascimento:
                self.__tela_jogador.mostra_mensagem("Jogador já cadastrado!")
                self.__controlador_sistema.abre_opcoes()
                return

        jogador = Jogador(dados_jogador["nome"], data_nascimento, dados_jogador["senha"], pontuacao=0)
        self.__jogadores.append(jogador)
        self.__tela_jogador.mostra_mensagem("\nCadastro realizado com sucesso!")
        self.__tela_jogador.mostra_mensagem("Faça Login para jogar! \n")
        
    def altera_cadastro(self):
        pass

    def remove_jogador(self):
        pass

    def ordena_ranking(self):
        self.lista_jogadores.sort(key=lambda jogador: (
            jogador.pontuacao, jogador.nome))

    def lista_jogadores(self):
        for jogador in self.__jogadores:
            self.__tela_jogador.mostra_mensagem({"nome": jogador.nome})

    def estah_cadastrado(self, nome, senha):
        for jogador in self.__jogadores:
            if jogador.nome == nome and jogador.senha == senha:
                return True
