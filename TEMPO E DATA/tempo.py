# correto
import datetime
from datetime import timedelta

horas, minutos, segundos = map(int, input("Informe o tempo: ").split(":")) # o map transforma a lista de numeros em int
# No codigo de cima a funcao map vai pegar o "[01:30:10]" -> ["01", "30", "10"],
# ou seja, a lista de str (feita pelo metodo .split()) se transforma numa lista de inteiros

tempo = timedelta(hours = horas, minutes = minutos, seconds = segundos)
print(f"Você correu por {horas}h.")