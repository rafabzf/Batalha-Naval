from entidade.oceano import Oceano

class TelaEmbarcacao:
    def mostra_embarcacoes(self):
       embarcacoes = Oceano.embarcacoes()
       return embarcacoes 
    
    def recebe_posicao_embarcacao(self):
        print("Informe a posição para inserir o barco: ")
        linha = int(input("Linha: "))
        coluna = input("Coluna: ").upper()
        return linha, coluna
        
        '''
        print("Qual embarcação você deseja posicionar?")
        print("Escolha uma das opções:")
        print("1 - Bote")
        print("2 - Submarino")
        print("3 - Fragata")
        print("4 - Bote")
        posicao = int(input("Opção número: "))
        if posicao == 1:
            print("Escolha 1 posição para inserir o Bote: ")
            coluna = input("Informe a coluna: ")
            linha = int(input("Informe a linha: "))
        elif posicao == 2:
            print("Escolha 2 posições para inserir o Submarino: ")
            coluna = input("Informe a coluna: ")
            linha = int(input("Informe a linha: "))
        elif posicao == 3:
            print("Escolha 3 posições para inserir a Fragata: ")
        elif posicao == 4:
            print("Escolha 4 posições para inserir o Porta-aviões: ")
        else:
            print("Opção inválida!")
        '''
    
    def mostra_embarcacoes_disponiveis(self, embarcacoes):
        pass