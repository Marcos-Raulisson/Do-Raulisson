# Importando a biblioteca pytest
import pytest
# Importando o .py com a função de soma
import teste

# objeto da classe teste
obj = teste.teste()

# primeiro teste


def teste1():
    assert 10 == obj.metodo_multiplicacao(2, 5)

# teste com erro


def teste2():
    assert 11 == obj.metodo_multiplicacao(3, 5)
