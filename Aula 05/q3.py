# Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

operacao = input("Digite uma operação: (+, -, *, /)")

if operacao == "+":
    resultado = num1 + num2
    print(f"A soma de {num1} + {num2} é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"A subtraçao de {num1} + {num2} é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"A multiplicação de {num1} + {num2} é: {resultado}")
elif operacao == "/":
    if num2 == 0:
        print('Nao é possível dividir por zero')
    else:
        resultado = num1 / num2
        print(f"A divisao de {num1} / {num2} é: {resultado}")