#ola profe jiji juju jojo

import math
print("------------------------------------------------------------")
print("Wena wena companiero ahora vamos a jugar el juego de amongu   \nel juego trata de pillar a un asesino por turnos\nel juego consta de 2 personas y simplemente gana el que gana")
print("------------------------------------------------------------")
participante1 = float(input("Ingresa el tiempo en minutos del participante 1: "))
participante2 = float(input("Ingresa el tiempo en minutos del participante 2: "))

minutosTotales = participante1 + participante2

horas = minutosTotales / 60

print("------------------------------------------------------------")
print("Ahora tenemos que calcular el peso de los participantes")


PesoParticipante1 = float(input("Ingresa el peso del participante 1: "))
PesoParticipante2 = float(input("Ingresa el peso del participante 2: "))
print("------------------------------------------------------------")
print("Ahora necesitamos tu percepcion del esfuerzo del 1-10")

PercepcionParticipante1 = float(input("Ingresa la percepcion del participante 1: "))
PercepcionParticipante2 = float(input("Ingresa la percepcion del participante 2: "))
print("------------------------------------------------------------")

esfuerzo1 = 1.5 + 0.4 * PercepcionParticipante1**1.3 

esfuerzo2 = 1.5 + 0.4 * PercepcionParticipante2**1.3 

Energia1 = PercepcionParticipante1 * horas * esfuerzo1 

Energia2 = PercepcionParticipante2 * horas * esfuerzo2 

energiapromedio = (Energia1 + Energia2) / 2
print("Ahora veamos de cuantos puntos va a tener")

cantidadDeAcciones = float(input("Ingresa la cantidad de acciones que hicieron 1: "))
rotacion = float(input("Ingresa la cantidad de rotaciones que hicieron del 0 al 5: "))
seguridad = float(input("Ingresa la cantidad de seguridad que tuvieron del 0 al 5: "))


puntajebase = 2000 + 300 * cantidadDeAcciones + 1200 + rotacion * 1000 

sinergia = 0

if puntajebase < 10000:
        sinergia = puntajebase * 0.08
        
elif puntajebase < 20000 and puntajebase > 10000:
        sinergia = puntajebase * 0.1
        
elif puntajebase> 20000:
        sinergia = puntajebase * 0.12

puntajetotal = puntajebase + sinergia

puntajebonos = 0

if minutosTotales > 45:
    puntajebonos= puntajebonos + 500
    
if rotacion > 4 or seguridad < 3:
    puntajebonos = puntajebonos + 300
#quiero completos pipipipi
print("------------------------------------------------------------")
print("Ahora veamos los tiempos de armado")
armas = int(input("Ingresa la cantidad de armas que dejarán en el mapa: "))
elementos = int(input("Ingresa la cantidad maxima de elementos a instalar por minuto: "))
tiempoarmado= armas/elementos
print("------------------------------------------------------------")

round(Energia1,2)
round(Energia2, 2)
print("------Ahora pasaremos todos los indicadores finales :D------")

horas = round(horas)
minutosTotales = minutosTotales % 60
print("El tiempo total que pasaron jugando es:",horas,"horas y", minutosTotales, "minutos.")
print("La energia total del jugador 1 es de:", round(Energia1,2))
print("La energia total del jugador 2 es de:", round(Energia2,2))
print("La energia promedio de los jugadores es de:", round(energiapromedio,2))
print("El puntaje base fue de:", round(puntajebase,2))
print("El puntaje total fue de:", round(puntajetotal,2))
print("El puntaje con bonos fue fue de:", round(puntajebase+puntajebonos,2))
print("El tiempo de armado es de:", tiempoarmado)

#naa k buen codigo, claramente me merezco un completo, ire por uno :D
