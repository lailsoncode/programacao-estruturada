# Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. O idioma é opcional e padrão para "inglês". A função deve retornar uma saudação no idioma especificado.

def saudacao_personalizada(nome, idioma="inglês"):
    if idioma == "português":
        return f"Olá, {nome}!"
    elif idioma == "inglês":
        return f"Hello, {nome}!"
    elif idioma == "espanhol":
        return f"Hola, {nome}!"
    else:
        return f"Hello, {nome}!"
    
nome = input("Digite seu nome: ")
idioma = input("Digite o idioma (português, inglês ou espanhol): ")

print(saudacao_personalizada(nome, idioma))