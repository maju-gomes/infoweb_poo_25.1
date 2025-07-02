class Frete:
    def __init__(self, distancia, peso):
        self.set_distancia(distancia)
        self.set_peso(peso)

    def set_distancia(self):
        if self.__distancia <= 0:
            raise ValueError("Valor inválido")
        
    def set_peso(self, peso):
        if self.__peso <= 0:
            raise ValueError("Valor inválido")
        
    def get_distancia(self, distancia):
        return self.__distancia
    
    def get_peso(self):
        return self.__peso

    def calcular_frete(self):
        frete = 0.01 * self.__distancia * self.__peso
    
    def __str__(self):
        return f"O valor do frete é {frete.calcular_frete()}"


frete = Frete(100, 50)

