#Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).

nota = int(input("Digite a nota:"))
if nota >= 90 and nota <= 100:
    print('A')
elif nota >= 80 and nota <= 89:
    print('B')
elif nota >= 70 and nota <= 79:
    print('C')
elif nota >= 60 and nota <= 69:
    print('D')
else:
    print('F')