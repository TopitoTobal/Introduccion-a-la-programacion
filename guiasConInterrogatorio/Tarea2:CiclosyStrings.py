# --- ENTRADAS ---
# Declaramos los inputs que salen en el pdf sisi
dimension = int(input("Ingrese dimension del cuadrado para el tablero: "))
texto_tablero = input("Tablero: ")

# Pedimos las coordenadas una por una para no usar funciones raras sisi
x_inicio = int(input("Ingrese coordenada de inicio x: "))
y_inicio = int(input("Ingrese coordenada de inicio y: "))
energia = int(input("Energia inicial: "))

# --- VALIDACIONES DE INICIO ---
# Vamos a ver si todo ta gud antes de iniciar el juego de amongu sisi
todo_ok = True

if dimension < 3:
    todo_ok = False
elif len(texto_tablero) != dimension * dimension:
    todo_ok = False
elif "C" not in texto_tablero:
    todo_ok = False
elif not (0 <= x_inicio < dimension and 0 <= y_inicio < dimension):
    todo_ok = False
elif energia <= 0:
    todo_ok = False

if todo_ok:
    indice_inicio = y_inicio * dimension + x_inicio
    if texto_tablero[indice_inicio] != "T":
        todo_ok = False

if not todo_ok:
    print("Configuracion inicial invalida")
else:
    # --- ARMANDO EL MAPA ---
    # Pasamos el texto a una matriz pa trabajar como pro sisi
    tablero = []
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            caracter = texto_tablero[i * dimension + j]
            fila.append(caracter)
        tablero.append(fila)

    x_actual = x_inicio
    y_actual = y_inicio
    
    total_checkpoints = 0
    for caracter in texto_tablero:
        if caracter == "C":
            total_checkpoints += 1
            
    checkpoints_logrados = 0
    
    # Creamos el tablero donde marcamos la J sisi
    tablero_final = []
    for f in range(dimension):
        fila_copia = []
        for c in range(dimension):
            fila_copia.append(tablero[f][c])
        tablero_final.append(fila_copia)
    
    tablero_final[y_actual][x_actual] = "J"

    # --- BUCLE DEL JUEGO ---
    # Sin usar continue, usamos puros if/else para filtrar los movimientos sisi
    while checkpoints_logrados < total_checkpoints and energia > 0:
        movimiento = input("Movimiento (udlr): ")
        
        if movimiento not in ["u", "d", "l", "r"]:
            print("Movimiento debe ser (u)p, (d)own, (1) left, o (r)ight")
        else:
            # Calculamos pa donde se quiere mover el tripulante sisi
            nuevo_x = x_actual
            nuevo_y = y_actual
            
            if movimiento == "u": nuevo_y -= 1
            elif movimiento == "d": nuevo_y += 1
            elif movimiento == "l": nuevo_x -= 1
            elif movimiento == "r": nuevo_x += 1
            
            # Validamos si el movimiento es posible dentro del tablero y sin muros
            if not (0 <= nuevo_x < dimension and 0 <= nuevo_y < dimension) or tablero[nuevo_y][nuevo_x] == "M":
                print("Movimiento invalido")
            else:
                # Si el movimiento es legal, vemos si gasta energia sisi
                if tablero_final[nuevo_y][nuevo_x] != "J":
                    costo = 1
                    if tablero[nuevo_y][nuevo_x] == "A":
                        costo = 2
                    energia -= costo
                    
                    if tablero[nuevo_y][nuevo_x] == "C":
                        checkpoints_logrados += 1
                        print("Checkpoint alcanzado")

                # Actualizamos la posicion siempre que el movimiento sea valido
                x_actual = nuevo_x
                y_actual = nuevo_y
                tablero_final[y_actual][x_actual] = "J"

    # --- RESULTADOS FINALES ---
    if checkpoints_logrados == total_checkpoints:
        print("¡Mapa finalizado!")
    else:
        print("Energia agotada")
        
    print("Tablero final:")
    for fila in tablero_final:
        linea = ""
        for item in fila:
            linea += item
        print(linea)
        
    print("Energia final:", energia)
