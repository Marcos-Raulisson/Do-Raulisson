# from getpass import getpass
# import os

# user_registrado = ['admin']
# password_registrado = ['admin']

# while True:

#     print('Seja bem vindo ao Banco Central')
#     i = input('Tecle:\n'
#               '[E] - Entrar\n'
#               '[C] - Cadastrar\n'
#               '[X]- Sair: ').upper()

#     if i == 'E':
#         print('Por favor insira seu usuário!')

#         user_digitado = input('Usuário: ')
#         password_digitado = getpass('Senha: ')

#         while user_digitado in user_registrado and password_digitado in password_registrado:
#             os.system('clear')
#             print('Você entrou')
#             saldo = 1000
#             credito = 1000

#             i = input('Deseja fazer alguma opção?\n'
#                       '[S] - Para ver o saldo\n'
#                       '[C] - Para ver o crédito\n'
#                       '[T] - Para fazer transferência: ').upper()

#             if i == 'S':
#                 print(f'Seu saldo está no valor total de:{saldo}')
#                 break
#             elif i == 'C':
#                 print(f'Seu crédito está no valor total de:{credito}')
#                 break
#             elif i == 'T':
#                 print('Vou fazer a transferência!')
#                 break
#             else:
#                 print('Nenhuma opção selecionada')
#                 break
#         else:
#             print('Usuário ou senha incorreta')

#     elif i == 'C':
#         print('Vamos começar o seu cadastro')
#         usuario = input('Digite um NOVO usuário: ')
#         senha = getpass('Digite uma NOVA senha: ')

#         user_registrado.append(usuario)
#         password_registrado.append(senha)
#         os.system('clear')
#         print('NOVO USUÁRIO CADASTRADO!')
#         continue
#     else:
#         print('Volte sempre!')
#         break
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")