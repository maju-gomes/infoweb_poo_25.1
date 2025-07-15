import datetime
# ERRADO:
# data = datetime(input())

# correto:
data = datetime.strp(input(), "%d/%m/%Y") #datetime é str
print(data.strftime("%d/%m/%Y")) # o datetime se transforma em str


