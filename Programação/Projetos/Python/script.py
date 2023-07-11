def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    return imc


def interpretar_imc(imc):
    # Interpreta o IMC e retorna uma mensagem
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"


# Solicita os dados de peso e altura ao usuário
peso = float(input("Digite o peso em kg: "))
# Adicionar valor em metros (Ex: 1.83)
altura = float(input("Digite a altura em metros: "))

# Chama a função para calcular o IMC
imc = calcular_imc(peso, altura)

# Interpreta o IMC
resultado = interpretar_imc(imc)

# Exibe o resultado
print("O seu IMC é:", imc)
print("Classificação:", resultado)
