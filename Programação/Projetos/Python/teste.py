from getpass import getpass
import os

banco = {}


def cadastro(banco):

    banco['new_user'] = input('Digite um novo usuário: ')
    banco['new_password'] = input('Digite uma nova senha: ')

    return banco


def login():
    print('Insira seu usuário e senha.')

    banco['user'] = input('Digite seu usuário: ')
    banco['password'] = input('Digite sua senha: ')

    return banco


if banco['user'].keys() == banco['new_user'].keys():
    print('Você entrou')

print(banco)

# print('Seja bem vindo ao Banco Central')
# i = input('Tecle:\n'
#           '[E] - Entrar\n'
#           '[C] - Cadastrar\n'
#           '[S] - Sair').upper()

# if i == 'E':
#     return login()
