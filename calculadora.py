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

print("Calculadora Simples")
print("Operações disponíveis:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

operacao = input("Selecione a operação desejada (1/2/3/4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

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
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print(f"\n{num1} {simbolo} {num2} = {resultado}")