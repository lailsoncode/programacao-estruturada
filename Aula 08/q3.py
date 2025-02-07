# 3- Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da seguinte forma: cada célulaé a soma dela mesma e das células anteriores. Imprima o vetor antes e depois da manipulação. Exemplo:

# Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
# Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]

import random
lista = [random.randint(0,20) for i in range(10)]

print(f"Vetor original {lista}")

for i in range(1, len(lista)):
    lista[i] += sum(lista[:i])

print(f"Vetor manipulado {lista}")