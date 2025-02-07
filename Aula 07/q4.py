# Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente]

def potencia(base, expoente=2):
    return base ** expoente

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
print(potencia(base, expoente))