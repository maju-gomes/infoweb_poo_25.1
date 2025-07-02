# Entrada dos números
numeros = input("Digite 4 números separados por espaço: ")
numeros = list(map(int, numeros.split()))
c_numeros = len(numeros)

# Ordenação com bubble sort
for i in range(c_numeros - 1):
    for j in range(c_numeros - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Cálculo da média
soma = 0
for num in numeros:
    soma += num
media = int(soma / c_numeros)

# Verifica números maiores ou iguais à média
num_maiores_ou_iguais = []
for num in numeros:
    if num >= media:
        num_maiores_ou_iguais.append(str(num))

# Verifica números menores que a média
num_menores = []
for num in numeros:
    if num < media:
        num_menores.append(str(num))

# Exibe os resultados
print(f"Média: {media:.2f}")
print("Números maiores ou iguais à média:", ", ".join(num_maiores_ou_iguais) if num_maiores_ou_iguais else "Nenhum")
print("Números menores que a média:", ", ".join(num_menores) if num_menores else "Nenhum")
