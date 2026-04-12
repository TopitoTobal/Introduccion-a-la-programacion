#vamo a declarar todos los inputs que salen en el pdf sisi
dimension = int(input("Ingrese dimensión del cuadrado para el tablero:"))
tablero = input("tablero:")
coordenadaInicial = input("coordenadas de inicio (x,y):")
energia = input("Energía inicial:")

#esto son variables inutiles pero utiles (iteradores y asi)
i = 0

checkpoint = 0


#ahora haremos las validaciones de inicio pa ver si ta todo gud e iniciar el juego de amongu sisi
if dimension*dimension > len(tablero) or dimension*dimension < len(tablero) or dimension < 3:
    print ("configuracion inicial invalida")

while i == len(tablero):
    if tablero[i] == T:
        checkpoint += 1
        i+= 1
        
if checkpoint == 0:
    print ("configuracion inicial invalida")


