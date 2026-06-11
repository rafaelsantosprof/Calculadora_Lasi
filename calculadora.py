# Projeto: calculadora com as quatro operações básicas e duas funções extras:
# 1ª calculo da distancia percorrida por um projétil;
# 2ª calculo do determinante de uma matriz.

# Para o 1º caso, será usada a biblioteca math.
import math

# Criando a função de verificação:
def verificar (numero):
    while True:
        try:
            valor = float(input(numero))
            return valor
        except:
            print("ERRO! Digite apenas números. \n")

# Definir cada função da calculadora:
def soma():
    numeroA = verificar("Digite o primeiro número:")
    numeroB = verificar("Digite o segundo número:")
    res_soma = float(numeroA) + float(numeroB)

    print(f"O resultado da soma é: {res_soma} \n")

soma()
# O código quebra quando o usuário digita uma letra ao invés de um número.
# Correção, criar uma nova função para tratar o erro, com try except.