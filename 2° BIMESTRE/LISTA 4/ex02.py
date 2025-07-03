class Contato:
    def __init__(self, id, nome, email, telefone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_telefone(self, telefone): self.__telefone = telefone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone}"

class ContatoUI:
    contatos = []

    @staticmethod
    def mostrar_menu():
        print("\n===== AGENDA DE CONTATOS =====")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Pesquisar")
        print("6 - Sair")

    @classmethod
    def adicionar(cls):
        id = input("ID: ")
        nome = input("Nome: ")
        email = input("Email: ")
        tel = input("Telefone: ")
        cls.contatos.append(Contato(id, nome, email, tel))
        print("Contato adicionado.")

    @classmethod
    def listar(cls):
        print("\n--- Lista ---")
        for c in cls.contatos:
            print(c)

    @classmethod
    def atualizar(cls):
        id = input("ID do contato para atualizar: ")
        for c in cls.contatos:
            if c.get_id() == id:
                c.set_nome(input("Novo nome: "))
                c.set_email(input("Novo email: "))
                c.set_telefone(input("Novo telefone: "))
                print("Contato atualizado.")
                return
        print("Contato não encontrado.")

    @classmethod
    def excluir(cls):
        id = input("ID do contato para excluir: ")
        novos = [c for c in cls.contatos if c.get_id() != id]
        if len(novos) < len(cls.contatos):
            cls.contatos = novos
            print("Contato excluído.")
        else:
            print("Contato não encontrado.")

    @classmethod
    def pesquisar(cls):
        ini = input("Iniciais do nome: ")
        encontrados = [c for c in cls.contatos if c.get_nome().startswith(ini)]
        if encontrados:
            for c in encontrados:
                print(c)
        else:
            print("Nenhum contato encontrado.")

    @classmethod
    def main(cls):
        while True:
            cls.mostrar_menu()
            op = input("Opção: ")
            if op == "1": cls.adicionar()
            elif op == "2": cls.listar()
            elif op == "3": cls.atualizar()
            elif op == "4": cls.excluir()
            elif op == "5": cls.pesquisar()
            elif op == "6":
                print("Saindo.")
                break
            else:
                print("Opção inválida.")

ContatoUI.main()
