from entendidade.embarcacao import Embarcao


class Oceano:
    def __init__(self, tamanho_oceano: int, embarcacoes: [Embarcao]):
        self.__tamanho_oceano = tamanho_oceano
        self.__embarcacoes = embarcacoes
        
    def embarcacoes(self):
        self.__embarcacoes = []
        return self.__embarcacoes
    
    def adiciona_embarcacao(self, tamanho: int, nome: str, posicoes: int):
        nova_embarcacao = Embarcao(tamanho, nome, posicoes)
        self.__embarcacoes.append(nova_embarcacao)
        