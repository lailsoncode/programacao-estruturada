#Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".

nome = input("Digite o nome de usuário:")
senha = input("Digite a senha:")
if nome == "admin" and senha == "12345":
    print('Acesso concedido')
else:
    print('Acesso negado')