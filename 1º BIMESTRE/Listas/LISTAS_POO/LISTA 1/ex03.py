class Conta:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

c = Conta("Lucas", "123")
c.depositar(100)
c.sacar(30)
print(f"Titular: {c.nome}, Conta: {c.numero}, Saldo: R${c.saldo}")
