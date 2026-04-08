import math

combustible = float(input())
rendimiento = float(input())
ciudadesVisitadas = 0

cordX = 0
cordY = 0
casillasResultado = combustible * rendimiento

seAgoto = False
volvioAlOrigen = False

while not seAgoto and not volvioAlOrigen:
    nuevaX = float(input())
    nuevaY = float(input())

    distancia = math.sqrt((nuevaX - cordX)**2 + (nuevaY - cordY)**2)

    if casillasResultado >= distancia:
        casillasResultado -= distancia
        cordX = nuevaX
        cordY = nuevaY
        
        if cordX == 0 and cordY == 0:
            volvioAlOrigen = True
        else:
            ciudadesVisitadas = ciudadesVisitadas + 1
    else:
        seAgoto = True

print("Recorre", ciudadesVisitadas, "ciudades")

if volvioAlOrigen:
    print("Vuelve al punto de partida")
else:
    print("Combustible agotado")
