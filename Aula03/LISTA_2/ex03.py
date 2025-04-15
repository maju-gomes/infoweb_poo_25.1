import math

base_e_altura = ("Digite a base e a altura do retângulo: ")
base = int(input())
altura = int(input())

area = base * altura
perimetro = base * 2 + altura * 2

diagonal = math.sqrt(base**2 + altura**2)

print(f"Área: {area:.2f} - Perímetro: {perimetro:.2f} - Diagonal: {diagonal:.2f}")