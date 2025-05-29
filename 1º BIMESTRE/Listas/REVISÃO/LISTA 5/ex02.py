num1 = int(input("Digite três números: \n"))
num2 = int(input())
num3 = int(input())


def maior(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z
    
maior = maior(num1, num2, num3)
print(maior)