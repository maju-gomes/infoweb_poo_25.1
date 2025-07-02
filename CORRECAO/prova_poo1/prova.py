class Disciplina:
    def __init__(self, nome, n1, n2, nf):
        self.set_nome(nome)
        self.set_n1(n1)
        self.set_n2(n2)
        self.set_nf(nf)

    # getters e setters
    def set_nome(self, nome): #o self sempre recebe o parametro nome
        if nome == "": raise ValueError()
        self.__nome = nome

    def set_n1(self, n1):
        if n1 < 0 or n1 > 10: raise ValueError()

    def set_n2(self, n2):
        if n2 < 0 or n2 > 10: raise ValueError()

    def set_nf(self, nf):
        if nf < 0 or nf > 10: raise ValueError()

    def get_nome(self):
        return self.__nome
    def get_n1(self):
        return self.__n1
    def get_n2(self):
        return self.__n2
    def get_nf(self):
        return self.__nf

    def media(self):
        mp = (2 * self.__n1 + 3 * self.__n2) / 5
        if mp >= 60:
            return ( 1 * mp + 1 * self.__nf) / 2

    def __str__(self):
        return f"{self.__nome}: {self.__n1}, {self.__n2}, {self.__nf}"
    
class DisciplinaUI:
    @staticmethod
    def main():
        op = 0
        while op != "2":
            op = DisciplinaUI.menu()
            if op == "1":
                DisciplinaUI.calculo()
            else: break
    
    @staticmethod
    def menu():
        print("Escolhar um opção: ")
        escolha = int(input("1 - Disciplina, 2 - Fim\n"))
        return escolha
    
    @staticmethod
    def calculo(): # mwtodos chamados com sublinhados nsao sao chamados diretamente. 
        nome = int("Informe o nome da disciplina: ")
        n1 = int(input("informe a primeira nota: "))
        n2 = int(input("Informe a segunda nota: "))
        nf = int(input("Informe sua nota final: "))
        x = Disciplina(nome, n1, n2, nf)
        print(x)

DisciplinaUI.main()
        