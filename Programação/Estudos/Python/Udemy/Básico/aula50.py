"""
Execício
Exiba os índices da lista
0 Maria
1 Helena
2 Marcos
"""
lista = ['Maria', 'Helena', 'Marcos']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
