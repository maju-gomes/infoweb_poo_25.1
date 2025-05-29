import math

# Leitura das coordenadas dos pontos
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Calculando a distância entre os dois pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprimindo o resultado com 4 casas decimais
print(f"{distancia:.4f}")
