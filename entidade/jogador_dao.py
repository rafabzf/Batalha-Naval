from entidade.dao import DAO
from entidade.jogador import Jogador

class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador:Jogador):
        return super().add(jogador.nome, jogador)
    
    def get(self, nome:str):
        return super().get(nome)
    
    def remove(self, jogador):
        super().remove(jogador.nome)