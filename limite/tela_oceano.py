class TelaOceano:
    def mostra_opcoes(self):
        print("------Tela Oceano------")
        print("Selecione a opção desejada")
        print("1 - Criar Oceano Jogador")
        print("2 - Criar Oceano Computador")
        print("3 - Adicionar embarcação")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
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