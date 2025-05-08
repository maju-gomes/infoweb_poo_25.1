class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.tempo_horas = horas + minutos / 60

    def velocidade_media(self):
        return self.distancia / self.tempo_horas

distancia = float(input("Distância (km): "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

viagem = Viagem(distancia, horas, minutos)
print(f"Velocidade média: {viagem.velocidade_media():.2f} km/h")
