from oceano import Oceano


class Jogo:
    def __init__(self, nome: str, data_nascimento: str) -> None:
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__oceano = Oceano
        self.__pontuacao = pontuacao
        self.__senha = str
        self.historico = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @nome.setter
    def nome(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao
