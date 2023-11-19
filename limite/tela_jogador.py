'''class TelaJogador:
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
        print(msg)'''

import PySimpleGUI as sg

class TelaJogador:
    def __init__(self):
        sg.theme('DarkBlue')

    def recebe_cadastro(self):
        layout = [
            [sg.Text('------CADASTRO------')],
            [sg.Text('Digite seu nome:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite sua data de nascimento (DD/MM/AAAA):'), sg.Input(key='-NASCIMENTO-')],
            [sg.Text('Digite sua senha:'), sg.Input(key='-SENHA-')],
            [sg.Button('Cadastrar')],
        ]

        window = sg.Window('Cadastro', layout)

        event, values = window.read(close=True)
        if event == sg.WIN_CLOSED:
            return None

        nome = values['-NOME-']
        nascimento = values['-NASCIMENTO-']
        senha = values['-SENHA-']
        return {"nome": nome, "data_nascimento": nascimento, "senha": senha}

    def seleciona_jogador(self):
        layout = [
            [sg.Text('Digite o nome do Jogador:'), sg.Input(key='-NOME-')],
            [sg.Text('Digite a senha:'), sg.Input(key='-SENHA-')],
            [sg.Button('Selecionar')],
        ]

        window = sg.Window('Selecionar Jogador', layout)

        event, values = window.read(close=True)
        if event == sg.WIN_CLOSED:
            return None

        nome = values['-NOME-']
        senha = values['-SENHA-']
        return {"nome": nome, "senha": senha}

    def pega_dados_jogador(self):
        layout = [
            [sg.Text('----------- INSIRA OS SEGUINTES DADOS ------------')],
            [sg.Text('Nome do Player:'), sg.Input(key='-NOME-')],
            [sg.Text('Data de nascimento do player (##/##/####):'), sg.Input(key='-NASCIMENTO-')],
            [sg.Text('Senha:'), sg.Input(key='-SENHA-')],
            [sg.Button('Inserir')],
        ]

        window = sg.Window('Inserir Dados', layout)

        event, values = window.read(close=True)
        if event == sg.WIN_CLOSED:
            return None

        nome = values['-NOME-']
        nascimento = values['-NASCIMENTO-']
        senha = values['-SENHA-']
        return {"nome": nome, "nascimento" : nascimento, "senha": senha}

    def mostra_historico(self, historico):
        layout = [
            [sg.Text('Histórico de Partidas:')],
            [sg.Multiline(historico, size=(30, 10))],
            [sg.Button('Fechar')],
        ]

        window = sg.Window('Histórico de Partidas', layout)

        while True:
            event, _ = window.read(close=True)
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

    def mostra_pontuacao(self, pontuacao):
        layout = [
            [sg.Text('Pontuação:')],
            [sg.Text(pontuacao, key='-PONTUACAO-')],
            [sg.Button('Fechar')],
        ]

        window = sg.Window('Pontuação', layout)

        while True:
            event, _ = window.read(close=True)
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

    def mostra_lista_jogadores(self, lista_jogadores):
        layout = [
            [sg.Text('Lista de Jogadores:')],
            [sg.Listbox(lista_jogadores, size=(30, 10))],
            [sg.Button('Fechar')],
        ]

        window = sg.Window('Lista de Jogadores', layout)

        while True:
            event, _ = window.read(close=True)
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

    def mostra_mensagem(self, msg):
        sg.popup(msg)
