# Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.

def idade_valida(idade):
    if type(idade) == int and 0 <= idade <= 150:
        return True
    else:
        return False
    
idade = int(input("Digite sua idade: "))

if idade_valida(idade):
    print("Idade válida.")
else:
    print("Idade inválida.")
