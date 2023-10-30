'''
def programa1():
    numero = int(input('Digite um número: '))

    if (numero % 2) == 0:
        print('Par')
    else:
        print('Impar')


programa1()




def programa2():
    print('Seja bem vindo à Digo a Hora!')
    hora = int(input('Digite a hora atual: '))
    minutos = int(input('Digite quantos minutos são agora: '))

    if hora <= 12:
        print(f'Boa tarde {hora}-{minutos}')
    elif hora <= 6:
        print(f'Boa noite {hora}-{minutos}')
    else:
        print(f'Bom dia {hora}-{minutos}')


programa2()


def programa3():
    nome = input('Digite o seu primeiro nome: ')

    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <= 6:
        print('Seu nome é normal')
    elif len(nome) >= 8:
        print('Seu nome é grande')
    else:
        print('Nenhum valor encontrado')


programa3()
'''

# ATIVIDADE ORIGINAL

# PROGRAMA 1
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# PROGRAMA 2
# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

# PROGRAMA 3
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
