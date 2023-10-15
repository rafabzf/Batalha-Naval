from controle.controlador_oceano import ControladorOceano

class TelaOceano:
    def recebe_tamanho(self):
        print("-----TAMANHO DO OCEANO-----")
        tamanho = int(input("Informe o tamanho do oceano da partida: "))
        return tamanho
        
    def mostra_oceano_jogador(self):
        pass
    
    def mostra_oceano_computador(self):
        pass
    
    def mostra_mensagem(self):
        print("Oceano criado com sucesso!")