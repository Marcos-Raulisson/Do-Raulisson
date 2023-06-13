# In[1]
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Python in texto = {'Python' in texto}")

print(f"Quantidade de y n texto = {texto.count('y')}")

print(f"As 5 primeiras letras são:{texto[0:6]}\n")
# Na entrada 1, usamos algumas operações das sequências. A operação len() permite saber o tamanho da sequência. O operador 'in', por sua vez, permite saber se um determinado valor está ou não na sequência. O operador count permite contar a quantidade de ocorrências de um valor. E a notação com colchetes permite fatiar a sequência, exibindo somente partes dela. Na linha 6, pedimos para exibir da posição 0 até a 5, pois o valor 6 não é incluído.

# In[2]
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(texto.upper())
print(texto.replace("i", 'XX'))
# Podemos usar a função lower() para tornar um objeto str com letras minúsculas, ou, então, a função upper(), que transforma para maiúsculo. A função replace() pode ser usada para substituir um caractere por outro.

# In[3]
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"\n texto = {texto}")

print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()

print(f"palavras = {palavras}")

print(f"Tamanho de palavras = {len(palavras)} \n")
# Na linha 5 da entrada 3 (In [3]), usamos a função split() para cortar o texto e guardamos o resultado em uma variável chamada "palavras". Veja no resultado que o texto tem tamanho 60, ou seja, possui uma sequência de 60 caracteres. Já o tamanho da variável "palavras" é 8, pois, ao cortar o texto, criamos uma lista com as palavras (em breve estudaremos as listas). A função split(), usada dessa forma, corta um texto em cada espaço em branco.

# In[4]
texto = """Operadores de String Python oferece operadores para processarem texto(ou seja, valores de string). Assim como os números, as strings podem ser comparadas usando operadores de comparação: ==, !=, <, > e assim por diante. O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor(Perkovic, p.23, 2016)."""

print(f"Tamanho do texto = {len(texto)}")

texto = texto.lower()

texto = texto.replace(",", "").replace(".", "").replace(
    "(", "").replace(")", "").replace("\n", " ")

lista_palavras = texto.split()

print(f"Tamanho da lista de palavras = {len(lista_palavras)}")


total = lista_palavras.count("string") + lista_palavras.count("strings")


print(f"Quantidade de vezes que string ou strings aparecem = {total} \n")
"""
Na entrada 4 (In [4]), começamos criando uma variável chamada "texto" que recebe uma citação do livro: Introdução à computação usando Python: um foco no desenvolvimento de aplicações.

Na linha 8, aplicamos a função lower() a essa string para que todo o texto fique com letras minúsculas e guardamos o resultado dessa transformação, dentro da própria variável, sobrescrevendo, assim, o texto original.

Na linha 9, fazemos uma série encadeada de transformações usando a função replace(), que age substituindo o primeiro parâmetro pelo segundo. No primeiro replace(",", ""), substituímos todas as vírgulas por nada. Então, na verdade, estamos apagando as vírgulas do texto sem colocar algo no lugar. No último replace("\n", " "), substituímos as quebras de linhas por um espaço em branco.

Na linha 10 criamos uma lista ao aplicar a função split() ao texto. Nesse caso, sempre que houver um espaço em branco, a string será cortada, criando um novo elemento na lista. Veja no resultado que criamos uma lista com 58 elementos.

Na linha 13 está a "mágica": usamos a função count() para contar tanto a palavra "string" no singular quanto o seu plural "strings". Uma vez que a função retorna um número inteiro, somamos os resultados e os exibimos na linha 15.
"""
