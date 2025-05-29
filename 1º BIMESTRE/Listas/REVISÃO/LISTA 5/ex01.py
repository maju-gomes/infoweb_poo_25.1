num1 = int(input("Digite dois números: \n"))
num2 = int(input(""))


def maior(x, y):
    if x > y:
        return x
    else:
        return y
    
maior = maior(num1, num2)
print(maior)