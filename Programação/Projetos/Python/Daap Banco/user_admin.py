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
            json.dump(bd, arquivo, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    novo_usuario = Cadastro()  # Crie uma instância de Cadastro
    novo_usuario.save_log()
