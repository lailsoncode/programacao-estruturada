# Faça um programa que calcula a quantidade de divisores de um número (incluindo 1 e o próprio número) que são divisíveis por 3.
# Referência
# Formato de entrada
# O usuário deve digitar um inteiro N.
# Formato de saída
# O programa deve exibir um inteiro R, sendo R o número de divisores de N que são divisiveis por 3. Caso não tenha nenhum, imprima "O numero nao possui divisores multiplos de 3" sem as aspas.
# O programa deve imprimir
# Quantidade de divisores divisiveis por 3: n / O numero nao possui divisores multiplos de 3


#O número não possui divisores multiplos de 3
#Quantidade de divisores divisiveis por 3: 
numero = int(input("Digite um número: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0 and i % 3 == 0:
        divisores += 1

if divisores == 0:
    print("O numero nao possui divisores multiplos de 3")
else:
    print(f"Quantidade de divisores divisiveis por 3: {divisores}")
    