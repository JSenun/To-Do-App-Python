import json
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