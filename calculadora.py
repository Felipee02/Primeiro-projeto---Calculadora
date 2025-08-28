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
        return "Erro: divisão por zero"

def menu():
    print("=== Calculadora Simples ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Escolha uma operação: ")
    if escolha == "0":
        print("Saindo da calculadora...")
        break
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if escolha == "1":
        print("Resultado:", soma(num1, num2))
    elif escolha == "2":
        print("Resultado:", subtracao(num1, num2))
    elif escolha == "3":
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == "4":
        print("Resultado:", divisao(num1, num2))
    else:
        print("Opção inválida!")
    print("\n")
