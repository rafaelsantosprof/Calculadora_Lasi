#Calculadora LASI
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
    print("\n---Cálculo da soma---\n")
    numeroA = verificar("Digite o primeiro número:")
    numeroB = verificar("Digite o segundo número:")
    res_soma = float(numeroA) + float(numeroB)

    print(f"\nO resultado da soma é: {res_soma} \n")

def subtrair():
    print("\n---Cálculo da subtração---\n")
    numeroA = verificar("Digite o primeiro número:")
    numeroB = verificar("Digite o segundo número:")
    res_sub = float(numeroA) - float(numeroB)

    print(f"\nO resultado da subtração é: {res_sub} \n")

def multiplicar():
    print("\n---Cálculo da multiplicação---\n")
    numeroA = verificar("Digite o primeiro número:")
    numeroB = verificar("Digite o segundo número:")
    res_mult = float(numeroA) * float(numeroB)

    print(f"\nO resultado da multiplicação é: {res_mult} \n")

def dividir():
    print("\n---Cálculo da Divisão---\n")
    numeroA = verificar("Digite o primeiro número:")
    numeroB = verificar("Digite o segundo número:")
    res_div = float(numeroA) / float(numeroB)

    print(f"\nO resultado da divisão é: {res_div} \n")



# Primeira parte da calculadora concluído
# Adicionar funções extras:
def fisica():
    print("\n---Cálculo da distância percorrida por um projétil---\n")
    # Variáveis:
    gravidade = 9.8 #Constante
    velocidade = verificar("Digite a velocidade inicial: \n") #Fornecido pelo usuário
    angulo = verificar("Digite o ângulo em graus:\n") #Fornecido pelo usuário
    radianos = math.radians(angulo) #Uso da biblioteca por questões de bloqueio trigonométrico
    

    #Fazendo V ao quadrado:
    numeroA = velocidade * velocidade
    #Calculando o seno de 2vezes o ângulo:
    numeroB = math.sin(2 * radianos)

    resultado = (numeroA * numeroB) / gravidade

    print(f"\nA distancia percorrida pelo projétio foi de: {resultado}m \n")



    #para calcular o determinate
def submatriz(matriz, col_remover):
    return [
        linha[:col_remover] + linha[col_remover + 1 :] for linha in matriz[1:]
    ]


def calcular_det(matriz):

    ordem = len(matriz)
    if ordem == 1:
        return matriz[0][0]
    if ordem == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0
    for col in range(ordem):
        sinal = 1 if col % 2 == 0 else -1
        sub = submatriz(matriz, col)
        det += sinal * matriz[0][col] * calcular_det(sub)
    return det


def determinate():
    print("\nCálculo do determinante\n")

    #pedir a ordem da matri
    ordem = int(verificar("Digite a ordem da matriz quadrada (ex: 2, 3, 4): "))

    #monta a matri a partir das informações do usuário
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            elemento = verificar(f"Digite o elemento da posição [{i+1}][{j+1}]: ")
            linha.append(elemento)
        matriz.append(linha)

    #printa a matri na tela
    print("\nMatriz informada:")
    for linha in matriz:
        print(linha)

    #resultado
    resultado = calcular_det(matriz)
    print(f"\nO determinante da matriz é: {resultado} \n")



#Criando o Menu:
def menu():

    while True:
        print("*** CALCULADORA LASI ***")
        print("Opção 1: Soma")
        print("Opção 2: Subtração")
        print("Opção 3: Multiplicação")
        print("Opção 4: Divisão")
        print("Opção 5: Distancia percorrida por um projétil")
        print("Opção 6: Determinante de matriz")
        print("Opção 7: Sair do programa\n")

        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == '1':
            soma()

        elif opcao == '2':
            subtrair()

        elif opcao == '3':
            multiplicar()

        elif opcao == '4':
            dividir()

        elif opcao == '5':
            fisica()

        elif opcao == '6':
            determinate()

        elif opcao == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida\n")

menu()