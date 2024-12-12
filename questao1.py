# Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

numero = input("Digite um número: ")
if numero == numero[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")

        #     '121':'True\n',
        # '-121':'False\n',
        # '10':'False\n',
        # '010101010':'True\n',
        # '01':'False\n',
        # '1':'True\n',
        # '-1':'False\n',