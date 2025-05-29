class Conta:
    def __init__(self, titular, numero, saldo):
        self.__titular = ""
        self.__numero = ""
        self.__saldo = 0.0

    def set_titular(self, titular):
        if titular == "":
            raise ValueError("O nome não pode ser vazio")
        self.__titular = titular

    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Digite um valor válido")
        self.__saldo += valor 