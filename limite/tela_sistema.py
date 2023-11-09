class TelaSistema:
    def mostra_opcoes(self):
        print("------Batalha Naval------")
        print("Selecione a opção desejada")
        print("1 - Fazer Login")
        print("2 - Fazer Cadastro")
        print("3 - Remover Cadastro")
        print("0 - Encerrar o sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao
