from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador


class ControladorJogador:
    def __init__(self):
        self.__tela_jogador = TelaJogador()
        self.__jogadores = []

    def cadastra_jogador(self):
        dados_cadastro = self.__tela_jogador.recebe_cadastro()
        try:
            jogador = Jogador(
                dados_cadastro["nome"], dados_cadastro["data_nascimento"], dados_cadastro["senha"])
            self.__jogadores.append(jogador)
            self.__tela_jogador.mostra_mensagem("\nCadastro realizado com sucesso!")
            self.__tela_jogador.mostra_mensagem("Faça Login para jogar! \n")
        except:
            self.__tela_jogador.mostra_mensagem("ERRO: Jogador não cadastrado!")

    def altera_cadastro(self):
        pass

    def remove_jogador(self):
        pass

    def ordena_ranking(self):
        #Use o método `sort` para ordenar com base na pontuação e, em seguida, no nome.
        self.lista_jogadores.sort(key=lambda jogador: (jogador.pontuacao, jogador.nome))

    def lista_jogadores(self):

        for jogador in self.__jogadores:
            self.__tela_jogador.mostra_mensagem({"nome": jogador.nome})
    

    def estah_cadastrado(self, nome, senha):          
        for jogador in self.__jogadores:
            print(jogador)
            if jogador.nome == nome and jogador.senha == senha:
                return True
                
    
    