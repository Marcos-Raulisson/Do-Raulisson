"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona pop no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Creat  Read Update   Delete
Criar, Ler, aletrar, apagar = lista[i] (CRUD)

Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (muntável)
"""
lista_a = ['Marcos', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
