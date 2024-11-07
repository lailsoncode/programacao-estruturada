#Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.

num1 = int(input("Digiteo primeiro numero:"))
num2 = int(input("Digiteo segundo numero:"))
num3 = int(input("Digiteo terceiro numero:"))

if num1 > num2 and num1 > num3:
    print(f'{num1} é maior que {num2} e {num3}')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é maior que {num1} e {num3}')
else:
    print(f'{num3} é maior que {num1} e {num2}')