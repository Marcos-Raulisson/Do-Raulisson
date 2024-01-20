from getpass import getpass
import os

usuario = {'new_user': '',
           'new_password': '',
           'user': '',
           'password': ''
           }


def cadastro():
    # Cria o cadastro de novos clientes e leva para o dicionário 'usuario'
    print('Por favor, insira as informações abaixo.')
    new_user = input('Digite um NOVO usuário: ')
    new_password = getpass('Digite uma NOVA senha: ')

    usuario.update({'new_user': new_user})
    usuario.update({'new_password': new_password})
    print('Você criou uma conta.')
    print('')

    return login()


def validacao():
    # Valida se o usuário e a senha criado estão cadastrados dentro do usuario
    while usuario == '':
        print('Essa conta não existe\n'
              'Por favor crie uma nova conta.')
        print('')
        return cadastro()

    if usuario['user'] == usuario['new_user'] and usuario['password'] == usuario['new_password']:
        print('Você entrou')
        return 0

    else:
        escolha = input('Usuário ou senha incorreto.\n'
                        'Crie uma nova conta ou tente outra vez.\n'
                        '[T] - Tentar de novo.\n'
                        '[N] - Nova conta: ').upper()

        if escolha == 'T':
            os.system('clear')
            return login()
        else:
            os.system('clear')
            return cadastro()


def login():
    print('Insira o seu usuário e senha.')
    # Insere e valida se o usuário está cadastrado no 'banco'
    usuario['user'] = input('Digite seu usuário: ')
    usuario['password'] = getpass('Digite sua senha: ')
    os.system('clear')
    return validacao()


while True:
    print('Seja bem vindo ao Banco Central')
    escolha = input('Tecle:\n'
                    '[E] - Entrar\n'
                    '[C] - Cadastrar\n'
                    '[S] - Sair: \n').upper()

    if escolha == 'E':
        os.system('clear')
        login()
    elif escolha == 'C':
        os.system('clear')
        cadastro()
    elif escolha == 'S':
        os.system('clear')
        print('Volte sempre!\n')
        break
    else:
        os.system('clear')
        print('Opção incorreta, tente outra vez\n')
