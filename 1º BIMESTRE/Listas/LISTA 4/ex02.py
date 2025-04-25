a, b = map(int, input("Digite dois números: ").split())

if a % b == 0 or b % a == 0:
    print("São Multiplos")
else:
    print("Não sao Multiplos")
