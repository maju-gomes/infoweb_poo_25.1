def formatar_nome(nome):

    preposicoes = {'de', 'da', 'das', 'do', 'dos', 'e', 'a', 'as', 'o', 'os'}

    partes = nome.lower().split()
    nome_formatado = []

    for i, palavra in enumerate(partes):
        if i == 0 or palavra not in preposicoes:
            nome_formatado.append(palavra.capitalize())
        else:
            nome_formatado.append(palavra)

    return ' '.join(nome_formatado)

nome_usuario = input("Digite seu nome completo: ")

nome_formatado = formatar_nome(nome_usuario)

print(f"Nome formatado: {nome_formatado}")
