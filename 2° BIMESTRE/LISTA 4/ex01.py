import random

class Bingo:
    def __init__(self):
        self.__numBolas = 0
        self.__bolas_sorteadas = []

    def set_numBolas(self, numBolas):
        if numBolas > 0:
            self.__numBolas = numBolas
        else: raise ValueError("O número de bolas não pode ser zero.")
    def get_numBolas(self):
        return self.__numBolas
    
    def get_bolas_sorteadas(self):
        return self.__bolas_sorteadas
    
    #MÉTODOS

    def iniciar(self, numBolas):
        self.set_numBolas(numBolas)
        self.__bolas_sorteadas = []
        print(f"Jogo iniciado com {numBolas} bolas.")
    
    def sortear(self):
        if len(self.__bolas_sorteadas) >= self.__numBolas:
            return "Todas as bolas já foram sorteadas."

        while True:
            bola = random.randint(1, self.__numBolas)
            if bola not in self.__bolas_sorteadas:
                self.__bolas_sorteadas.append(bola)
                return bola

    def sorteados(self):
        return self.__bolas_sorteadas
    
    def __str__(self):
        return f"Bingo com {self.__numBolas} bolas. Números sorteados até agora: {self.__bolas_sorteadas}."
        
class BingoUI:

    bingo = Bingo()

    @staticmethod
    def main():
        
        while True:
            BingoUI.menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                BingoUI.iniciar_jogo()
            elif opcao == "2":
                BingoUI.sortear()
            elif opcao == "3":
                BingoUI.sorteados()
            elif opcao == "4":
                print("Saindo do jogo")
                break

    @staticmethod
    def menu():
        print("Bem-vindo ao jogo Bingo")
        print("1 - Iniciar o jogo")
        print("2 - Sortear um numero")
        print("3 - Ver numeros sorteados")
        print("4 - Sair")

    @staticmethod
    def iniciar_jogo():
        num = int(input("Quantas bolas tera o jogo? "))
        BingoUI.bingo.iniciar(num)

    @staticmethod
    def sortear():
        resultado = BingoUI.bingo.sortear()
        print(f"Numero sorteado: {resultado}")

    @staticmethod
    def sorteados():
        bolas = BingoUI.bingo.get_bolas_sorteadas()
        print(f"Bolas sorteadas até agora: {bolas}")

BingoUI.main()