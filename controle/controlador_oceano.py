from limite.tela_embarcacao import TelaEmbarcacao
from limite.tela_oceano import TelaOceano

class ControladorOceano:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__tela_oceano = TelaOceano()
    
    def cria_oceano(self, tamanho_oceano):
        oceano = [['O' for _ in range(tamanho_oceano)] for _ in range(tamanho_oceano)]
        return oceano

    def cria_oceano_jogador(self):
        tamanho_oceano = self.__tela_oceano.recebe_tamanho()
        oceano_jogador = self.cria_oceano(tamanho_oceano)
        coluna_letras = [chr(65 + i) for i in range(tamanho_oceano)]
        print("  " + " ".join(coluna_letras))

        for i in range(tamanho_oceano):
            linha = [str(i + 1)] + oceano_jogador[i]
            print(" ".join(linha))
        return oceano_jogador

    def cria_oceano_computador(self):
        tamanho_oceano = self.__tela_oceano.recebe_tamanho()
        oceano_computador = self.cria_oceano(tamanho_oceano)
        coluna_letras = [chr(65 + i) for i in range(tamanho_oceano)]
        print("  " + " ".join(coluna_letras))

        for i in range(tamanho_oceano):
            linha = [str(i + 1)] + oceano_computador[i]
            print(" ".join(linha))
        return oceano_computador

    def adiciona_embarcacao_oceano(self):
        pass
    
    def adiciona_embarcacao_oceano_computador(self):
        pass
    
    def abre_tela(self):
        lista_opcoes = {1: self.cria_oceano_jogador, 2: self.cria_oceano_computador, 3: self.adiciona_embarcacao_oceano}
        while True:
            try:
                opcao_escolhida = self.__tela_oceano.mostra_opcoes()
                if opcao_escolhida not in lista_opcoes:
                    raise ValueError
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except ValueError:
                self.__tela_oceano.mostra_mensagem("Valor inválido, digite um número válido")