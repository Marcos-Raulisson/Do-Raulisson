
def inicio():
    def login():
        user_digitado = input('Usuário: ')
        password_digitado = input('Senha: ')

        password_permitida = user_digitado
        user_permitido = password_digitado

        if user_digitado in user_permitido and password_digitado == password_permitida:
            print('Você entrou')
        else:
            print('Usuário incorreto')
        return inicio()

    def cadastro():
        nome_completo = input('Digite seu nome completo:')
        usuario = input('Digite seu nome de usuário:')
        senha = input('Digite sua senha:')

        novo_user = (nome_completo, usuario, senha)
        print('Você cadastrou um novo usuário')
        return login()

    entrada = input(
        'Seja bem vindo ao Banco do Raulisson. Você tem uma conta?[S]im ou [N]ão?')
    if entrada == 'S' or entrada == 's':
        print('Faça o login')
        return login()

    elif entrada == 'N' or entrada == 'n':
        print('Você não entrou')
        entrada = input(
            'Usuário ou senha incorreto. Deseja cadastrar novo usuário?[S]im ou [N]ão?')

        if entrada == 'S' or entrada == 's':
            return cadastro()
    else:
        print('Nenhuma opção selecionada!')
        return inicio()


inicio()

# requisições


def require():
    user = {}
    password = {}
