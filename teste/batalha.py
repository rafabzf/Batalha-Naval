import random

class Embarcacao:
    def __init__(self, nome, sigla, tamanho, quantidade):
        self.nome = nome
        self.sigla = sigla
        self.tamanho = tamanho
        self.quantidade = quantidade

class Jogo:
    def __init__(self) -> None:
        self.__embarcacoes = [
            Embarcacao("Porta-Aviões", "P", 4, 1),
            Embarcacao("Fragata", "F", 3, 2),
            Embarcacao("Submarino", "S", 2, 2),
            Embarcacao("Bote", "B", 1, 3),
        ]

    def recebe_tamanho_oceano(self):
        tamanho_oceano = int(input("Digite o tamanho do oceano: "))
        return tamanho_oceano

    def criar_oceano(self, tamanho):
        return [["~" for _ in range(tamanho)] for _ in range(tamanho)]

    def imprimir_tabuleiro(self, oceano):
        tamanho = len(oceano)
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Usaremos letras para as colunas
        print("   " + " ".join(letras[:tamanho]))

        for i, linha in enumerate(oceano):
            # Use {:2} para formatar a largura da coluna em 2 caracteres
            print("{:2} {}".format(i, " ".join(linha)))

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
    
    def trata_coordenada(self, tamanho_oceano, msg):
        while True:
            try:
                coordenada = self.recebe_coordenada(msg)
                if len(coordenada) < 1 or not coordenada[1:].isdigit():
                    raise ValueError("Digite uma coordenada válida")
                linha = int(coordenada[1:])
                coluna = self.mapear_letra_numero(coordenada[0])
                if 0 <= linha < tamanho_oceano and 0 <= coluna < tamanho_oceano:
                    return linha, coluna
                else:
                    print("Coordenadas fora dos limites do tabuleiro. Tente novamente.")
            except ValueError as e:
                print(e)
        

    def posiciona_embarcacao(self, oceano, embarcacao):
        tamanho_oceano = len(oceano)
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


    def main(self):

        tamanho = self.recebe_tamanho_oceano()
        oceano_jogador = self.criar_oceano(tamanho)
        oceano_computador = self.criar_oceano(tamanho)
        self.imprimir_tabuleiro(oceano_jogador)


        for embarcacao in self.__embarcacoes:
            quantidade = embarcacao.quantidade
            for restante in range(quantidade, 0, -1):
                nome_embarcacao = embarcacao.nome
                tamanho_embarcacao = embarcacao.tamanho
                print(f"Quantidade de {nome_embarcacao} para serem posicionados: {restante}")
                print(f"Posicione o {nome_embarcacao} (tamanho {tamanho_embarcacao})")
                while True:
                    if self.posiciona_embarcacao(oceano_jogador, embarcacao):
                        self.imprimir_tabuleiro(oceano_jogador)
                        break

if __name__ == "__main__":
    Jogo().main()
