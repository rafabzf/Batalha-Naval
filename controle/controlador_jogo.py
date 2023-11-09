#from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo


class ControladorJogo:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__pontuacao_partida_jogador = 0
        self.__pontuacao_partida_computador = 0
        self.__pontuacao_total_computador = 0

    def faz_login(self):
        dados_login = self.__tela_jogo.recebe_login()
        recebe_nome, recebe_senha = dados_login["recebe_nome"], dados_login["recebe_senha"]
        if self.__controlador_sistema.retorna_estah_cadastrado(recebe_nome, recebe_senha):
            self.inicia_jogo()
        else:
            
            self.__tela_jogo.mostra_mensagem("Jogador não encontrado!")
            if self.__tela_jogo.voltar() == "S":
                self.__controlador_sistema.abre_opcoes()
            else:
                self.faz_login()
            
                
        


    def inicia_jogo(self):
        self.abre_opcoes()

    def voltar(self):
        self.faz_login()


    def abre_opcoes(self):
        lista_opcoes = {1: self.inicia_partida, 
                        2: self.mostra_ranking,
                        0: self.voltar}
        opcao_selecionada = self.__tela_jogo.mostra_opcoes()
        funcao_escolhida = lista_opcoes[opcao_selecionada]
        funcao_escolhida()

    def inicia_partida(self):
        self.__tela_jogo.mostra_mensagem("Partida iniciada!")
        self.__controlador_sistema.retorna_armazena_tamanho_oceano()
        self.__



    def mostra_ranking(self):
        self.__controlador_sistema.retorna_lista_jogadores()
        
        if self.__tela_jogo.voltar() == "S":
            self.abre_opcoes()
        else:
            self.__controlador_sistema.encerra_sistema()
        

    def realiza_jogada(self):
        acertou = False
        if acertou == True:
            self.__pontuacao_partida_jogador += 1



    def partida(self):
        pass
      
 
    def partida(self):
        pass
