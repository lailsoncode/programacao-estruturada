# 1- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1

# Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
# Leia um número do teclado
# Compare se este número está na lista

lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

x = int(input("Digite o número que deseja encontrar: "))
if x in lista:
    print(f"O número {x} está na posição {lista.index(x)}")
else:
    print(-1)