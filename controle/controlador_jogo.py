#from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
import random
from controle.controlador_oceano import ControladorOceano

class ControladorJogo:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogo = TelaJogo()
        self.__controlador_oceano = ControladorOceano
        self.__pontuacao_partida_jogador = 0
        self.__pontuacao_partida_computador = 0


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
        self.partida()
        #self.__controlador_sistema.retorna_armazena_tamanho_oceano()

    def mostra_ranking(self):
        self.__controlador_sistema.retorna_lista_jogadores()

        if self.__tela_jogo.voltar() == "S":
            self.abre_opcoes()
        else:
            self.__controlador_sistema.encerra_sistema()
        



    def imprimir_tabuleiro(self, tamanho, oceano):
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Usaremos letras para as colunas
        print("   " + " ".join(letras[:tamanho]))
        for i, linha in enumerate(oceano):
            # Use {:2} para formatar a largura da coluna em 2 caracteres
            print("{:2} {}".format(i, " ".join(linha)))
        print("   " + " ".join(letras[:tamanho]))

    def mapear_letra_numero(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 9:
            alfabeto = {i: chr(65 + i) for i in range(26)}
            if valor in alfabeto:
                return alfabeto[valor]
        elif isinstance(valor, str) and len(valor) == 1 and valor.isalpha():
            valor = valor.upper()  # Converte a letra para maiúscula
            alfabeto = {chr(65 + i): i for i in range(26)}
            if valor in alfabeto:
                return alfabeto[valor]  
        return None
    
    def recebe_coordenada(self, msg=None):
        while True:
            try:
                coordenada = input(f"Digite a coordenada {msg} desejada: ")
                return coordenada
            except ValueError as e:
                print(e)
    
    def trata_coordenada(self, tamanho_oceano, msg=None):
        while True:
            try:
                coordenada = self.recebe_coordenada(msg)
                if len(coordenada) < 2 or not coordenada[1:].isdigit() or not coordenada[0].isalpha():
                    raise ValueError("Digite uma coordenada válida")
                linha = int(coordenada[1:])
                coluna = self.mapear_letra_numero(coordenada[0])
                if 0 <= linha < tamanho_oceano and 0 <= coluna < tamanho_oceano:
                    return linha, coluna
                else:
                    print("Coordenadas fora dos limites do tabuleiro. Tente novamente.")
            except ValueError as e:
                print(e)
        

    def posiciona_embarcacao(self, tamanho_oceano, oceano, embarcacao):
        tamanho_embarcacao = embarcacao.tamanho
        sigla_embarcacao = embarcacao.sigla
        while True:
            linha_inicial, coluna_inicial = self.trata_coordenada(tamanho_oceano, msg="inicial")
            linha_final, coluna_final = self.trata_coordenada(tamanho_oceano, msg="final")
            break
        if (linha_inicial == linha_final and coluna_final - coluna_inicial == tamanho_embarcacao - 1) or \
            (coluna_inicial == coluna_final and linha_final - linha_inicial == tamanho_embarcacao - 1):
            for linha in range(linha_inicial, linha_final + 1):
                for coluna in range(coluna_inicial, coluna_final + 1):
                    if oceano[linha][coluna] != "~":
                        print("Posição já ocupada. Tente novamente.")
                        return False

                for linha in range(linha_inicial, linha_final + 1):
                    for coluna in range(coluna_inicial, coluna_final + 1):
                        oceano[linha][coluna] = sigla_embarcacao
                return True
        else:
            print("Posição inválida. Tente novamente.")

    def posiciona_embarcacao_computador(self, tamanho_oceano, oceano, embarcacao):
        tamanho_embarcacao = embarcacao.tamanho
        sigla_embarcacao = embarcacao.sigla

        while True:
            linha_inicial = random.randint(0, tamanho_oceano)
            coluna_inicial = random.randint(0, tamanho_oceano)
            orientacao = random.choice(["horizontal", "vertical"])

            if orientacao == "horizontal":
                linha_final = linha_inicial
                coluna_final = coluna_inicial + tamanho_embarcacao - 1
            else:
                linha_final = linha_inicial + tamanho_embarcacao - 1
                coluna_final = coluna_inicial

            if (0 <= linha_inicial < tamanho_oceano) and (0 <= coluna_inicial < tamanho_oceano) and \
            (0 <= linha_final < tamanho_oceano) and (0 <= coluna_final < tamanho_oceano):
                valido = True
                for linha in range(linha_inicial, linha_final + 1):
                    for coluna in range(coluna_inicial, coluna_final + 1):
                        if oceano[linha][coluna] != "~":
                            valido = False
                            break

                if valido:
                    for linha in range(linha_inicial, linha_final + 1):
                        for coluna in range(coluna_inicial, coluna_final + 1):
                            oceano[linha][coluna] = sigla_embarcacao
                    return True

    def fazer_tiro(self, tamanho_oceano, tabuleiro, oponente_tabuleiro):
        linha, coluna = self.trata_coordenada(tamanho_oceano, "do tiro")
        if oponente_tabuleiro[linha][coluna] != "~":
            tiro_acertou = True
            oponente_tabuleiro[linha][coluna] = "X"
            
        else:
            tiro_acertou = False
            oponente_tabuleiro[linha][coluna] = "O"
        tabuleiro[linha][coluna] = "X" if tiro_acertou else "O"
        return tiro_acertou

    def todas_embarcacoes_afundadas(self, tabuleiro):
        atingidas = 0
        for linha in tabuleiro:
            for simbolo in linha:
                if simbolo == "X":
                    atingidas += 1
        if atingidas ==  17:
            return True
    
    def vencedor(self, oceano_jogador, oceano_computador):
        if self.todas_embarcacoes_afundadas(oceano_jogador):
            print("Parabéns!!! Você venceu!")
    
            return True
        elif self.todas_embarcacoes_afundadas(oceano_computador):
            print("Você perdeu =(")
            return True

    

    def partida(self):       
        tamanho = self.__controlador_sistema.retorna_recebe_tamanho_oceano()
        oceano_jogador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_computador = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        oceano_oponente = self.__controlador_sistema.retorna_cria_oceano(tamanho)
        self.imprimir_tabuleiro(tamanho, oceano_jogador.matriz)

        for embarcacao in oceano_jogador.embarcacoes:  
            quantidade = embarcacao.quantidade
            for restante in range(quantidade, 0, -1):
                nome_embarcacao = embarcacao.nome
                tamanho_embarcacao = embarcacao.tamanho
                print(f"Quantidade de {nome_embarcacao} para serem posicionados: {restante}")
                print(f"Posicione o {nome_embarcacao} (tamanho {tamanho_embarcacao})")
                while True:
                    if self.posiciona_embarcacao(tamanho, oceano_jogador.matriz, embarcacao):
                        self.imprimir_tabuleiro(tamanho, oceano_jogador.matriz)
                        break
                
                self.posiciona_embarcacao_computador(tamanho, oceano_computador.matriz, embarcacao)  
            

        continua = True
        while continua:
            self.imprimir_tabuleiro(oceano_computador.matriz)
            self.fazer_tiro(tamanho, oceano_oponente.matriz, oceano_computador.matriz)
            self.imprimir_tabuleiro(tamanho, oceano_oponente.matriz)
            if self.vencedor(oceano_jogador.matriz, oceano_computador.matriz):
                continua = False
            
    
