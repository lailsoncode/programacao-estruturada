#Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.

lado1 = int(input("Digite o comprimento do primeiro lado:"))
lado2 = int(input("Digite o comprimento do segundo lado:"))
lado3 = int(input("Digite o comprimento do terceiro lado:"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado1 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Os lados não podem formar um triângulo')