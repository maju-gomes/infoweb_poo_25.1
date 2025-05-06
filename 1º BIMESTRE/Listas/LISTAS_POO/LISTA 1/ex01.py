import math
class Circulo:
    def __init__(self):
        self.raio = 0
    def area_circulo(self):
        area = round((self.raio**2 * math.pi), 2)
        return area
    def circunferencia_circulo(self):
        circ = round((2 * math.pi * self.raio), 2)
        return circ

x = Circulo()
x.raio = 10
print(f"A área do círculo é: {x.area_circulo()} \nA circunferência do círculo é: {x.circunferencia_circulo()}")