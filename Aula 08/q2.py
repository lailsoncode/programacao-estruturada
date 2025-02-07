# 2 - Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.

# Crie uma lista com tamanho 50 e armazene nesta lista valores gerados aleatóriamente
# Faça uma iteração na lista para verificar quantos destes números são iguais à 6

import random

lista = [random.randint(1, 6) for i in range(50)]
seis = lista.count(6)
print(lista)
percentual = seis / 50 * 100
print(f"O percentual de ocorrências do número 6 foi de {percentual:.2f}%")