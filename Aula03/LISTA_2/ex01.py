# 1ª resolução
nome_completo = input("Qual é o seu nome completo? ")
lista_nome = nome_completo.split()
primeiro_nome = lista_nome.pop(0)


print(f"Bem-vindo(a) ao Python, {primeiro_nome}!")

# split cria uma lista com uma cadeia de palavras (variavel.split())

# 2ª resolução
nome_completo = input("Qual é o seu nome completo? ")
lista_nome = nome_completo.split()
primeiro_nome = lista_nome[0]

print(f"Bem-vindo(a) ao Python, {primeiro_nome}!")