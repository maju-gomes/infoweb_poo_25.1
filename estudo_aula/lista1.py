# criando lista
# x = []
# x = list()

# valores em matriz
# [[1, 2, 3], [4, 5, 6]]
# x[1][2] ("printa" 6)

x = [1, 2, 3]
y = [6, 5, 4]

x = y[:] # x cria uma copia da lista y

sorted(x) # ordena a lista e cria outra a partir da que foi dada
print(id(x))
print(id(y))