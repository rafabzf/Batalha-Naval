class TelaJogador:
    def recebe_cadastro(self):
        print("------CADASTRO------")
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        senha = input("Digite sua data de senha: ")
        return {"nome": nome, "data_nascimento": data_nascimento, "senha": senha}
    
    def seleciona_jogador(self):
        print("--------------------------------------------------")
        nome = input("Digite o nome do Jogador: ")
        senha = input("Digite a senha: ")
        return {"nome": nome, "senha": senha}
    
    def pega_dados_jogador(self):
        print("----------- INSIRA OS SEGUINTES DADOS ------------")
        nome = input("Nome do Player: ")
        nascimento = input("Data de nascimento do player (##/##/####): ")
        senha = input("Senha: ")
        return {"nome": nome, "nascimento" : nascimento, "senha": senha}

    def mostra_historico(self):
        pass

    def mostra_pontuacao(self):
        pass
    
    def mostra_lista_jogadores(self):
        pass
 
    def mostra_mensagem(self, msg):
        print(msg)
