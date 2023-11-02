from limite.tela_embarcacao import TelaEmbarcacao
from limite.tela_oceano import TelaOceano

class ControladorOceano:
    def __init__(self, controlador_sistema):
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__tela_oceano = TelaOceano()
        
    '''def abre_tela(self):
        lista_opcoes = {1: self.jogada, 2:self.mostrar_jogadas, 3:self.mostrar_oceano, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_partida.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostra_mensagem("Valor inválido, digite um número Válido")'''
    
    def cria_oceano_jogador(self):
        tamanho_oceano = self.__tela_oceano.recebe_tamanho()
        oceano = [['O' for _ in range(tamanho_oceano)] for _ in range(tamanho_oceano)]
        coluna_letras = [chr(65 + i) for i in range(tamanho_oceano)]
        print("  " + " ".join(coluna_letras))

        for i in range(tamanho_oceano):
            linha = [str(i + 1)] + oceano[i]
            print(" ".join(linha))

        self.__controlador_sistema = controlador_sistema
        self.__tamanho_oceano = None
    
    
    def armazena_tamanho_oceano(self):
        self.__tamanho_oceano = self.__tela_oceano.recebe_tamanho()


    def cria_oceano(self):
        oceano = [['O' for _ in range(self.__tamanho_oceano)] for _ in range(self.__tamanho_oceano)]
        return oceano
    
    def cria_oceano_computador(self):
        tamanho_oceano = self.__tela_oceano.recebe_tamanho()
        oceano = [['O' for _ in range(tamanho_oceano)] for _ in range(tamanho_oceano)]
        coluna_letras = [chr(65 + i) for i in range(tamanho_oceano)]
        print("  " + " ".join(coluna_letras))

        for i in range(tamanho_oceano):
            linha = [str(i + 1)] + oceano[i]
            print(" ".join(linha))
    
    def adiciona_embarcacao_oceano(self):
        pass
    