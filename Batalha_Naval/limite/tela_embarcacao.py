from entidade.oceano import Oceano

class TelaEmbarcacao:
    def mostra_embarcacoes(self):
       embarcacoes = Oceano.embarcacoes()
       return embarcacoes 
    
    def recebe_posicao_embarcacao(self):
        pass