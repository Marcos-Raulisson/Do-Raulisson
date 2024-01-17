import json
import os
from user_admin import Cadastro

CAMINHO_ARQUIVO = 'mini_banco_dados.json'


def login_auth(user, password):
    
    with open(CAMINHO_ARQUIVO, 'r') as arquivo:
        login = json.load(arquivo)

        if user == new_user.Cadastro["new_user"] and password == new_password.Cadastro["new_user"]:
            print('Você entrou')
        else:
            print('erro')

    


while True:
    print('Seja bem vindo ao Banco Descentralizado\n')
    user = input('Digite seu usuário: ')
    password = input('Digite sua senha: ')

    login_auth(user, password)
    