import math
print("------------------------------------------------------------")
print("wena wena companiero ahora vamos a jugar el juego de amongu   \nel juego trata de pillar a un asesino por turnos\nel juego consta de 2 personas y simplemente gana el que gana")
print("------------------------------------------------------------")
participante1 = int(input("ingresa el tiempo en minutos del participante 1: "))
participante2 = int(input("ingresa el tiempo en minutos del participante 2: "))

minutosTotales = participante1 + participante2

horas = minutosTotales / 60

print (horas)

print("------------------------------------------------------------")
print("ahora tenemos que calcular el peso de los participantes")


PesoParticipante1 = int(input("ingresa el peso del participante 1: "))
PesoParticipante2 = int(input("ingresa el peso del participante 2: "))
print("------------------------------------------------------------")
print("ahora necesitamos tu percepcion del esfuerzo del 1-10")

PercepcionParticipante1 = int(input("ingresa la percepcion del participante 1: "))
PercepcionParticipante2 = int(input("ingresa la percepcion del participante 2: "))
print("------------------------------------------------------------")

esfuerzo1 = 1.5 + 0.4 * PercepcionParticipante1**1.3 

esfuerzo2 = 1.5 + 0.4 * PercepcionParticipante2**1.3 

Energia1 = PercepcionParticipante1 * horas * esfuerzo1 

Energia2 = PercepcionParticipante2 * horas * esfuerzo2 

