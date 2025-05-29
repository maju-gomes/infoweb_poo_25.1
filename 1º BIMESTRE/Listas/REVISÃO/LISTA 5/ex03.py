nome_completo = input("Qual é o seu nome completo? ")

lista_de_iniciais = []

def iniciais(nome):
    iniciais = nome.split()
    for inicial in iniciais:
        lista_de_iniciais.append(inicial[0])
    return ", ".join(lista_de_iniciais)
    
print(f"Suas iniciais são: {iniciais(nome_completo)}")