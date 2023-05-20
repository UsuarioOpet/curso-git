# Calculadora em Python

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def imprimir_menu():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    
def obter_operacao():
    operacao = input("Selecione a operação desejada (1/2/3/4): ")
    if operacao not in ["1", "2", "3", "4"]:
        raise ValueError("Operação inválida!")
    return operacao

def obter_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def calcular(operacao, num1, num2):
    if operacao == "1":
        resultado = soma(num1, num2)
        simbolo = "+"
    elif operacao == "2":
        resultado = subtracao(num1, num2)
        simbolo = "-"
    elif operacao == "3":
        resultado = multiplicacao(num1, num2)
        simbolo = "*"
    elif operacao == "4":
        resultado = divisao(num1, num2)
        simbolo = "/"
    return resultado, simbolo

def exibir_resultado(num1, simbolo, num2, resultado):
    print(f"\n{num1} {simbolo} {num2} = {resultado}")

def executar_calculadora():
    try:
        imprimir_menu()
        operacao = obter_operacao()
        num1, num2 = obter_numeros()
        resultado, simbolo = calcular(operacao, num1, num2)
        exibir_resultado(num1, simbolo, num2, resultado)
    except ValueError as error:
        print(f"Erro: {str(error)}")

executar_calculadora()