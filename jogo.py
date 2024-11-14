from random import randint
MAX_TENTATIVAS = 5
acertou = False
tentativas = 0

print("Bem-vindo ao jogo de adivinhação")
print("Adivinhe o número que estou pensando")
dificuldade = input("Escolha a dificuldade: fácil, médio ou difícil: ")
match dificuldade:
    case "fácil":
        MAX_TENTATIVAS = 10
        MIN, MAX = 0, 30
        numero = randint(0, 30)
    case "médio":
        MAX_TENTATIVAS = 5
        MIN, MAX = 0, 60
        numero = randint(0, 60)
    case "difícil":
        MAX_TENTATIVAS = 3
        MIN, MAX = 0, 100
        numero = randint(0, 100)
    case _:
        print("Dificuldade inválida")
        print("Escolhendo dificuldade média")
        MAX_TENTATIVAS = 5
        MIN, MAX = 0, 60
        numero = randint(0, 60)

print(f"Você escolheu a dificuldade {dificuldade}")
print(f"Estou pensando em um número entre {MIN} e {MAX}")

for tentativas in range(MAX_TENTATIVAS):
    chute = int(input(f"Digite um número entre {MIN} e {MAX} em {MAX_TENTATIVAS} tentativas: "))
    if chute < MIN or chute > MAX:
        print("Número inválido")
        continue
    if chute == numero:
        print(f"Parabéns, você acertou em {tentativas + 1} tentativas!")
        acertou = True
        break
    elif chute < numero:
        print("O número é maior")
    else:
        print("O número é menor")

# while not acertou and tentativas < MAX_TENTATIVAS:
#     chute = int(input(f"Digite um número entre {MIN} e {MAX} em {MAX_TENTATIVAS} tentativas: "))
#     if chute < MIN or chute > MAX:
#         print("Número inválido")
#         continue
#     tentativas += 1
#     if chute == numero:
#         print(f"Parabéns, você acertou em {tentativas} tentativas!")
#         acertou = True
#         break
#     elif chute < numero:
#         print("O número é maior")
#     else:
#         print("O número é menor")

if not acertou:
    print("Suas tentativas acabaram")
    print(f"O número era {numero}")