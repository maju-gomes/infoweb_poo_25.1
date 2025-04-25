nota_b1 = float(input("Digite a nota dos seus 2 bimetres:\n"))
nota_b2 = float(input())

def aprovado(nota1, nota2):
    if (nota1 + nota2) / 2 >= 60:
        return "aprovado"
    else:
        return "reprovado"
    
print(f"Você foi {aprovado(nota_b1, nota_b2)}")