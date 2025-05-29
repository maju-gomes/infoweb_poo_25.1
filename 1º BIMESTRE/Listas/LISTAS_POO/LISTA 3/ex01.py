import math 
class Retangulo:
    def __init__(self, base, altura):
        self.__base = 0
        self.__altura = 0
        self.set_base(base)
        self.set_altura(altura)

    def set_base(self, valor):
        if valor > 0:
            self.__base = valor
        else:
            raise ValueError("Digite um valor valido (positivo)")
        
    def set_altura(self, valor):
        if valor > 0:
            self.__altura = valor
        else:
            raise ValueError("Digite um valor valido (positivo)")
        
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def calcular_area(self):
        return self.__base * self.__altura 
    
    def calcular_diagonal(self):
        return math.sqrt(self.__base**2 + self._altura**2)
    
    def __str__(self):
        return f"A base do triângulo é {self.__base} e a altura é igual a {self.__altura}"

