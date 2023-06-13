# In[1]
import random
nomes = 'João Marcela Sonia Daryl Vernom Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split(
)

print('Marcela' in nomes)

print('Roberto' in nomes)
"""
A entrada 1 (In [1]), usamos o operador in para verificar se dois nomes constavam na lista. No primeiro, obtivemos True; e no segundo, False.
"""

# In[2]


def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False


# In[3]
lista = random.sample(range(1000), 50)

print(sorted(lista))

executar_busca_linear(lista, 10)

"""
Na entrada 2 (In [2]) criamos a função "executar_busca_linear", que recebe uma lista e um valor a ser localizado. Na linha 2, criamos a estrutura de repetição, que percorrerá cada elemento da lista pela comparação com o valor buscado (linha 3). Caso este seja localizado, então a função retorna o valor booleano True; caso não seja encontrado, então retorna False.

Para testarmos a função, criamos o código na entrada 3 (In[3]), no qual, por meio da biblioteca random (não se preocupe com a implementação, já que ainda veremos o uso de bibliotecas), criamos uma lista de 50 valores com números inteiros randômicos que variam entre 0 e 1000; e na linha 5 invocamos a função, passando a lista e um valor a ser localizado. Cada execução desse código gerará uma lista diferente, e o resultado poderá ser alterado.
"""

# In[4]

vogais = 'aeiou'

resultado = vogais.index('e')
print(resultado)
"""
A função index() espera como parâmetro o valor a ser procurado na sequência.
"""

# In[5]


def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
    return None


# In[6]
vogais = 'aeiou'
resultado = procurar_valor(lista=vogais, valor='u')
if resultado != None:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")
"""
Na entrada 5 (In [5]), criamos a função "procurar_valor", a fim de retornar a posição de um valor, caso ele seja encontrado. Na entrada 6 (In [6]), criamos uma lista com as vogais e invocamos a função "procurar_valor", passando a lista e um valor a ser procurado. Na linha 5, testamos se existe valor na variável "resultado", já que, caso o valor guardado em "resultado" for None, então o else é acionado.
"""
