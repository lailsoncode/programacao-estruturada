# Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido. Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com

def validar_email(email):
    if " " in email or email.count("@") != 1 or not email.endswith(".com"):
        return False
    else:
        return True
    
email = input("Digite seu email: ")

if validar_email(email):
    print("Email válido.")
else:
    print("Email inválido.")
