import json
import os

CAMINHO_ARQUIVO = 'mini_banco_dados.json'

class Cadastro:
    def __init__(self, new_user, new_password):
        self.new_user = new_user
        self.new_password = new_password

def save_log():
    new_user = input('Novo usuário: ')
    new_password = input('Nova senha: ')        
    pessoa = Cadastro(new_user, new_password)
    bd = [vars(pessoa)]        
    
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(bd, arquivo, indent = 2, ensure_ascii=False)

if __name__=='__main__':
    save_log()
