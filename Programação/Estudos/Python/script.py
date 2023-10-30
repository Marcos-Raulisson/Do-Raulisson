def inicio():
    print('seja bem vindo a calculadora do terminal!')
    a = int(input('Digite um número: '))
    sim = input('Escolha uma operação: ')
    b = int(input('Digite outro número:'))

    def escolha():
        choice = input('Deseja fazer uma nova operação. [S]im ou [N]ão?')
        if choice == 'S' or choice == 's':
            return inicio()
        else:
            print('Volte sempre !!!')
            return 0

    if sim == '+':
        resultado = a + b
        print(f'A soma de {a} com {b} é igual à: {resultado}')
        return escolha()
    elif sim == '-':
        resultado = a - b
        print(f'A subtração de {a} com {b} é igual à: {resultado}')
        return escolha()
    elif sim == '*':
        resultado = a * b
        print(f'A multiplicação de {a} com {b} é igual à: {resultado}')
        return escolha()
    elif sim == '/':
        resultado = a / b
        print(f'A divisão de {a} com {b} é igual à: {resultado}')
        return escolha()
    else:
        print('Opção inválida')
        return inicio()


inicio()
