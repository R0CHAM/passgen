import random
import PySimpleGUI as sg
from datetime import datetime


class PassGen:
    def __init__(self):
        # layout da interface gráfica
        sg.theme('DarkGrey13')
        layout = [
            [sg.Text('Site/Software', size=(15,1)),
             sg.Input(key='site', size=(20,1))],
             [sg.Text('E-mail/Usuário', size=(15,1)),
             sg.Input(key='usuario', size=(20,1))],
             [sg.Text('Quantidade de Caracteres'),
             sg.Combo(values=list(range(4,31)), key='total_chars', default_value=4, size=(3,1))],
             [sg.Checkbox('Maiúsculo', default=True, size=(10,1), key='maiuscula', enable_events=True), 
             sg.Checkbox('Minúsculo', default=True, size=(10,1), key='minuscula', enable_events=True),
             sg.Checkbox('Números', default=True, size=(10,1), key='numeros', enable_events=True),
             sg.Checkbox('Caracteres Especiais', default=True, size=(20,1), key='especial', enable_events=True)],
             [sg.Output(size=(80,10))],
             [sg.Button('Gerar Senha'), sg.Button('Consultar Senhas')]
        ]
        # Declarar janela
        self.janela = sg.Window('Password Generator', layout) 

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
            if evento == 'Consultar Senhas':
                f = open('.\senhas.txt', 'r')
                print(f.read())
                #sg.popup('Erro!','Função ainda não disponível.')
                    

    def gerar_senha(self, valores):
        # Possibilidades das checkbox
        chars1 = 'ABCÇDEFGHIJKLMNOPQRSTUVWXYZ'
        chars2 = 'abcçdefghijklmnopqrstuvwxyz'
        chars3 = '0123456789'
        chars4 = '!@#$%&*'
        chars_list = ''

        # Adicionando listas conforme checkbox's checadas
        if (valores['maiuscula']) == True:
            chars_list += chars1
        if (valores['minuscula']) == True:
            chars_list += chars2
        if (valores['numeros']) == True:
            chars_list += chars3
        if (valores['especial']) == True:
            chars_list += chars4

        # Seleção dos elementos randômicos de acordo com número de caracteres solicitados
        new_pass = ''.join(random.choices(chars_list,k=int(valores['total_chars'])))
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        data_atual = datetime.now().replace(microsecond=0)
        with open(f'senhas.txt', 'a') as arquivo:
            arquivo.write(
                f"Site: {valores['site']} \nUsuario: {valores['usuario']} \nSenha: {nova_senha} \nAtualizado em: {data_atual} \n")
        print('Arquivo salvo!!!')

gen = PassGen()
gen.Iniciar()

