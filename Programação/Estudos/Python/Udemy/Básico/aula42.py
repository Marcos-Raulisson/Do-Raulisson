frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == '':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual


print('A letra que apareceu mais vezes foi '
      f'{letra_que_apareceu_mais_vezes} que apareceu '
      f'{qtd_apareceu_mais_vezes}x'
      )
