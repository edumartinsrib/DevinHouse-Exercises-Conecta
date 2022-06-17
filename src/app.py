import json
import os

usuario = {'nome': 'joao', 'sobrenome':'silva' ,'idade': 20}
caminho = os.path.dirname(os.path.abspath(__file__))

def gera_json(usuario):
    with open(f'{caminho}\dados.json', 'w') as arquivo:
        json.dump(usuario, arquivo)
        
gera_json(usuario)


def ler_json():
    with open(f'{caminho}\dados.json') as arquivo:
        return json.load(arquivo)

print(ler_json())