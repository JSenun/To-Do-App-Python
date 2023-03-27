import json
from datetime import datetime
import PySimpleGUI as sg
# Criando funções para ler e atualizar o arquivo 'db.json'

def le_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
    return dados


def atualiza_arquivo_json(nome_arquivo, dados_processados_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        dados = json.dumps(dados_processados_arquivo)
        dados = json.loads(dados)
        json.dump(dados, arquivo_json)
        
# Criando a variavel que vai conter os dados das tarefas
tarefas_db = le_arquivo_json('db.json')

# Função que cria a tarefa (Dicionário que vai ser adicionado ao DB)
def cria_tarefa(titulo_tarefa, desc_tarefa):
    data = datetime.now()
    dia = f"{data.day:02d}/{data.month:02d}/{data.year}"
    tarefa = {
        "titulo_tarefa": titulo_tarefa,
        "descricao_tarefa": desc_tarefa,
        "data_criacao": dia,
        "status_tarefa": "Pendente"
    }
    print(tarefa)
    return tarefa

# Testando função com  a interface básica
sg.theme('LightBlue3')

# Função que cria a janela do formulário de criação de tarefa
def form_criar_tarefa():
    layout = [
        [sg.Text("Titulo da tarefa: "), sg.Input(key='titulo_tarefa')],
        [sg.Text("Descrição da tarefa: "), sg.Input(key='desc_tarefa')],
        [sg.Button('Adicionar tarefa')]
    ]


    janela = sg.Window('To Do APP', layout)

    while True:
        eventos, valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Adicionar tarefa':
            titulo_tarefa = valores['titulo_tarefa']
            desc_tarefa = valores['desc_tarefa']
            cria_tarefa(titulo_tarefa, desc_tarefa)
    janela.close()
        
# Função que gera a janela principal do APP
def main():
    layout = [
        [sg.Text("To Do APP")],
        [sg.Button("Criar tarefa")]
    ]
    
    janela = sg.Window('To Do App', layout)
    
    while True:
        eventos, valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "Criar tarefa":
            form_criar_tarefa()
    janela.close()
    
if __name__ == '__main__':
    main()