'''class TelaJogo:
    def recebe_login(self):
        print("------LOGIN-------")
        recebe_nome = input("Digite seu nome: ")
        recebe_senha = input("Digite sua senha: ")
        return{"recebe_nome": recebe_nome, "recebe_senha": recebe_senha}

    def mostra_resultado_jogo(self):
        pass

    def mostra_pontuacao_jogada(self):
        pass

    def mostra_opcoes(self):
        print("------MENU JOGO------")
        print("Selecione a opção desejada")
        print("1 - Iniciar partida")
        print("2 - Ver ranking")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))
        return opcao


    def mostra_mensagem(self, msg):
        print(msg)

    def voltar(self):
        opcao = input("Deseja voltar? [S/N]").upper()
        return opcao'''
        
import PySimpleGUI as sg

class TelaJogo:
    def recebe_login(self):
        layout = [
            [sg.Text('------LOGIN------')],
            [sg.Text('Digite seu nome:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua senha:'), sg.Input(key='-SENHA-')],
            [sg.Button('Login')],
        ]

        window = sg.Window('Login', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Login':
                recebe_nome = values['-NOME-']
                recebe_senha = values['-SENHA-']
                window.close()
                return {"recebe_nome": recebe_nome, "recebe_senha": recebe_senha}

    def mostra_resultado_jogo(self):
        pass

    def mostra_pontuacao_jogada(self):
        pass

    def mostra_opcoes(self):
        layout = [
            [sg.Text('------MENU JOGO------')],
            [sg.Text('Selecione a opção desejada')],
            [sg.Button('Iniciar partida')],
            [sg.Button('Ver ranking')],
            [sg.Button('Voltar')],
        ]

        window = sg.Window('Menu do Jogo', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Iniciar partida':
                window.close()
                return 1
            if event == 'Ver ranking':
                window.close()
                return 2
            if event == 'Voltar':
                window.close()
                return 0

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    def voltar(self):
        layout = [
            [sg.Text('Deseja voltar?')],
            [sg.Button('Sim'), sg.Button('Não')],
        ]

        window = sg.Window('Voltar', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Sim':
                window.close()
                return "S"
            if event == 'Não':
                window.close()
                return "N"
