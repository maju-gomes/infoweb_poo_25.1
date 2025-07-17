from datetime import datetime, timedelta

class Treino:
    def __init__(self, id_treino, data_treino, distancia_percorrida, tempo_corrida):
        self.__id_treino = id_treino
        self.__data_treino = data_treino
        self.__distancia_percorrida = distancia_percorrida
        self.__tempo_corrida = tempo_corrida


    # set
    def set_id_treino(self, id_treino):
        if id_treino < 1: raise ValueError() # não usa-se self.__ pq aqui verificamos o parametro atribuido ao set.
        self.__id_treino = id_treino

    # gets
    def get_id_treino(self):
        return self.__id_treino
    
    def get_data_treino(self):
        return self.__data_treino
    
    def get_distancia_percorrida(self):
        return self.__distancia_percorrida
    
    def get_tempo_corrida(self):
        return self.__tempo_corrida

    def __str__(self):
        return f"A corrida de id {self.__id_treino} realizada em {self.__data_treino} teve {self.__distancia_percorrida} percorridos e durou {self.__tempo_corrida}."
    
    # CLASS UI
    class TreinoUI:
        __treinos = []

        @classmethod
        def main(cls):
            opcao = 0
            while opcao != 7:
                opcao = TreinoUI.menu()
                if opcao == 1: TreinoUI.inserir()
                if opcao == 2: TreinoUI.listar()
                if opcao == 3: TreinoUI.listar_id()
                if opcao == 4: TreinoUI.atualizar()
                if opcao == 5: TreinoUI.excluir()
                if opcao == 6: TreinoUI.mais_rapido()
                if opcao == 7:
                    print("Programa finalizado")
                    break
                if opcao < 1 or opcao > 7: print("Digite um número válido")

        @classmethod
        def menu(cls):
            print("\n1 - Inserir um treino\n2 - Listar os treinos\n3 - Listar o id dos treinos\n4 - Atualizar algum treino\n5 - Excluir algum treino\n6 - Mostrar o mais rápido\n7 - Sair")
            return int(input("\nEscolha um desses acima:"))

        @classmethod
        def inserir(cls):
            id = int(input("Qual é o id do treino? "))
            data = in

        @classmethod
        def listar(cls):
            pass

        @classmethod
        def listar_id(cls):
            pass

        @classmethod
        def atualizar(cls):
            pass

        @classmethod
        def excluir(cls):
            pass

        @classmethod
        def mais_rapido(cls):
            pass

    