import json
import os

CAMINHO_ARQUIVO = 'mini_banco_dados.json'

class Cadastro:
    def __init__(self):
        self.new_user = input('Digite um novo usuário: ')
        self.new_password = input('Digite uma nova senha: ')
        os.system('clear')
        print('Usuário cadastrado com sucesso!')
    
    def save_log(self):
        bd = [vars(self)]  # Use 'self' para referenciar a instância atual

        with open(CAMINHO_ARQUIVO, 'a+', encoding='utf-8') as arquivo:
            if arquivo.tell() > 0:
                arquivo.write('\n')
            json.dump(bd, arquivo, indent=2, ensure_ascii=False)

def login():
    user_input = input('Digite seu usuário: ')
    password_input = input('Digite sua senha: ')

    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        try:
            bd_user = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            bd_user = []

    for user_data in bd_user:
        if user_data['new_user'] == user_input and user_data['new_password'] == password_input:
            print('VOCÊ ENTROU')
            return True  # Retorna True se o login for bem-sucedido
    print('Usuário ou senha incorretos.')
    return False  # Retorna False se o login falhar

if __name__ == '__main__':
    while True:
        print('Seja bem vindo ao Banco Descentralizado')
        escolha = input('Tecle:\n'
                        '[E] - Entrar\n'
                        '[C] - Cadastrar\n'
                        '[S] - Sair: \n').upper()

        if escolha == 'E':
            os.system('clear')
            if login():
                break  # Sai do loop se o login for bem-sucedido
        elif escolha == 'C':
            os.system('clear')
            novo_usuario = Cadastro()
            novo_usuario.save_log()
        elif escolha == 'S':
            os.system('clear')
            print('Volte sempre!\n')
            break  # Sai do loop se a opção for 'S'
        else:
            os.system('clear')
            print('Opção incorreta, tente outra vez\n')
   
    