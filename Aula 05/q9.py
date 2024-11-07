#Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC). Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.

peso = float(input("Digite o peso (em kg):"))
altura = float(input("Digite a altura (em metros):"))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print('Obeso')
else:
    print('Muito obeso')