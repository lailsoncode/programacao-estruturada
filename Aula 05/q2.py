#Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar.

num = int(input("Digite um número:"))
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')