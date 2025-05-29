class Triangulo():
    def __init__(self):
        self.base = 0
        self.altura = 0
    def calc_area(self):
        return self.base * self.altura / 2  
    def set_b(self, b):
        if base < 0: raise ValueError("A base não pode ser negativa")