import math

a, b, c = map(float, input("Quem é a, b e c, respectivamente? ").split())

delta = b**2 - 4*a*c

if delta >= 0 and a != 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
else:
    print("Impossivel calcular")
