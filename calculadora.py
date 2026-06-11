# Projeto: calculadora com as quatro operações básicas e duas funções extras:
# 1ª calculo da distancia percorrida por um projétil;
# 2ª calculo do determinante de uma matriz.

# Para o 1º caso, será usada a biblioteca math.
import math

# Definir cada função:
def soma():
    numeroA = float(input("Digite o primeiro número:"))
    numeroB = float(input("Digite o segundo número:"))
    res_soma = float(numeroA) + float(numeroB)

    print(f"O resultado da soma é: {res_soma} \n")

soma()
