class TelaJogador:
    def recebe_cadastro(self):
        print("------CADASTRO------")
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        senha = input("Digite sua data de senha: ")
        return {"nome": nome, "data_nascimento": data_nascimento, "senha": senha}

    def mostra_historico(self):
        pass

    def mostra_pontuacao(self):
        pass
    
    def mostra_lista_jogadores(self):
        pass
 
    def mostra_mensagem(self, msg):
        print(msg)
