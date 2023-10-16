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
        while True:
            tamanho = int(input("Informe o tamanho do oceano da partida: "))
            if tamanho < 6:
                print('Oceano pequeno demais, insira um valor entre 6 e 9')
            elif tamanho > 9:
                print('Oceano grande demais, insira um valor entre 6 e 9')
            else:
                return tamanho

    def mostra_mensagem(self, msg):
        print(msg)