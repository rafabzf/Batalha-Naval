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
        print("  " + " ".join(letras[:tamanho]))
        for i, linha in enumerate(oceano):
            print(i, " ".join(linha))

    def mapear_letra_numero(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 9:
            colunas = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
            if valor in colunas:
                return colunas[valor]
        elif isinstance(valor, str) and len(valor) == 1 and valor.isalpha():
            valor = valor.upper()  # Converte a letra para maiúscula
            colunas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
            if valor in colunas:
                return colunas[valor]
        return None
    
    def recebe_coordenada(self):
        coordenada = input("Digite a cordenada desejada: ")
        return coordenada
    
    def trata_coordenada(self, tamanho_oceano, coordenada):
        linha = int(coordenada[1])
        coluna = self.mapear_letra_numero(coordenada[0])
        if linha > tamanho_oceano or coluna > tamanho_oceano:
            print("Coordenadas fora dos limites do tabuleiro. Tente novamente.")
        else:
            return linha, coluna


    def posiciona_embarcacao(self, oceano, embarcacao, coordenada_inicial, coordenada_final):
                tamanho_oceano = len(oceano)
                tamanho_embarcacao = embarcacao.tamanho
                sigla_embarcacao = embarcacao.sigla
                linha_inicial, coluna_inicial = self.trata_coordenada(tamanho_oceano, coordenada_inicial)
                linha_final, coluna_final = self.trata_coordenada(tamanho_oceano, coordenada_final)
                if (linha_inicial == linha_final and coluna_final - coluna_inicial == tamanho_embarcacao - 1) or \
                    (coluna_inicial == coluna_final and linha_final - linha_inicial == tamanho_embarcacao - 1):
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
                    else:
                        print("Posição já ocupada. Tente novamente.")
                else:
                    print("Posição inválida. Tente novamente.")



    def main(self):

        tamanho = self.recebe_tamanho_oceano()
        oceano_jogador = self.criar_oceano(tamanho)
        #oceano_computador = self.criar_oceano(tamanho)
        self.imprimir_tabuleiro(oceano_jogador)


        for embarcacao in self.__embarcacoes:
            quantidade = embarcacao.quantidade
            for restante in range(quantidade, 0, -1):
                nome_embarcacao = embarcacao.nome
                tamanho_embarcacao = embarcacao.tamanho
                print(f"Quantidade de {nome_embarcacao} para serem posicionados: {restante}")
                print(f"Posicione o {nome_embarcacao} (tamanho {tamanho_embarcacao})")
                coordenada_inicial = self.recebe_coordenada()
                coordenada_final = self.recebe_coordenada()
                self.posiciona_embarcacao(oceano_jogador, embarcacao, coordenada_inicial, coordenada_final)
                self.imprimir_tabuleiro(oceano_jogador)
                

    
        
if __name__ == "__main__":
    Jogo().main()
