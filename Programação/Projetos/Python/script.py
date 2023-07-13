def cadastro():
    nome_completo = input('Digite seu nome completo:')
    usuario = input('Digite seu nome de usuário:')
    senha = input('Digite sua senha:')
    return login()


def login():
    user = input('Usuário: ')
    password = input('Senha: ')
    print('Você entrou')


def inicio():
    print('Seja bem vindo ao Banco do Raulisson. Você tem uma conta?')
    escolha1 = input()
    if escolha1 == 'y':
        return login()
    else:
        return cadastro()


inicio()

# requisições


def require():
    user = {}
    password = {}
