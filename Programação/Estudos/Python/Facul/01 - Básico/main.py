# O interpretador Python é capaz de determinar o tipo de dado da variável com base no seu valor, ou seja, as variáveis são tipadas dinamicamente nessa linguagem.

# In[2]
x = 10

nome = 'aluno'

nota = 8.75

fez_inscricao = True

# In[3]
print(type(x))

print(type(nome))

print(type(nota))

print(type(fez_inscricao))

# A célula de entrada 3 (In [3]) tem os comandos para imprimir na tela, os tipos das quatro variáveis que criamos anteriormente. Veja que foram impressas quatro diferentes classes de tipos de dados. A variável "x" é do tipo inteira (int). A variável "nome" é do tipo string (str). A variável "nota" é do tipo ponto flutuante (float). A variável "fez_inscricao" é do tipo booleana (bool).
# In[4]
nome = input("Digite um nome: ")

print(nome)
