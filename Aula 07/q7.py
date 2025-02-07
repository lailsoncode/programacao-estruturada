# Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. Forneça uma documentação estendida que explique como usar a função e inclua exemplos de uso.

def potencia(base, expoente=2):
    """
    Calcula a potência de um número elevado a uma potência especificada.
    
    Argumentos:
    base -- o número que será elevado à potência
    expoente -- a potência à qual a base será elevada (padrão 2)
    
    Exemplos:
    potencia(2, 3) retorna 8
    potencia(3) retorna 9
    """
    return base ** expoente

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
print(potencia(base, expoente))