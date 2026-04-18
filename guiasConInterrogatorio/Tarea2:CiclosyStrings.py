# --- ENTRADAS ---
# Lectura de los datos iniciales para el juego sisi
dimension = int(input("Ingrese dimension del cuadrado para el tablero: "))
texto_tablero = input("Tablero: ")

# Coordenadas de inicio ingresadas una por una jiji
x_inicio = int(input("Ingrese coordenada de inicio x: "))
y_inicio = int(input("Ingrese coordenada de inicio y: "))
energia = int(input("Energia inicial: "))

# --- VALIDACIONES DE INICIO ---
# Verificacion de las reglas de configuracion inicial ouchet
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
    # Calculo de posicion en el string para ver la casilla inicial sisi
    indice_inicio = y_inicio * dimension + x_inicio
    if texto_tablero[indice_inicio] != "T":
        todo_ok = False

if not todo_ok:
    print("Configuracion inicial invalida") # lol
else:
    # --- ARMANDO EL MAPA ---
    # Creacion de la matriz del tablero usando el texto ingresado jojo
    tablero = [None] * dimension
    for i in range(dimension):
        tablero[i] = [None] * dimension
        for j in range(dimension):
            tablero[i][j] = texto_tablero[i * dimension + j]

    x_actual = x_inicio
    y_actual = y_inicio
    
    # Conteo de checkpoints necesarios para ganar juju
    total_checkpoints = 0
    for caracter in texto_tablero:
        if caracter == "C":
            total_checkpoints += 1
            
    checkpoints_logrados = 0
    
    # Generacion del tablero final para el rastro del jugador sisi
    tablero_final = [None] * dimension
    for f in range(dimension):
        tablero_final[f] = [None] * dimension
        for c in range(dimension):
            tablero_final[f][c] = tablero[f][c]
    
    # Registro de la posicion inicial del tripulante lol
    tablero_final[y_actual][x_actual] = "J"

    # --- BUCLE DEL JUEGO ---
    # El juego sigue mientras queden checkpoints y energia ouchet
    while checkpoints_logrados < total_checkpoints and energia > 0:
        movimiento = input("Movimiento (udlr): ")
        
        # Validacion de los comandos permitidos jiji
        if movimiento != "u" and movimiento != "d" and movimiento != "l" and movimiento != "r":
            print("Movimiento debe ser (u)p, (d)own, (1) left, o (r)ight")
        else:
            nx = x_actual
            ny = y_actual
            
            if movimiento == "u": ny -= 1
            elif movimiento == "d": ny += 1
            elif movimiento == "l": nx -= 1
            elif movimiento == "r": nx += 1
            
            # Verificacion de limites y muros en el mapa sisi
            if not (0 <= nx < dimension and 0 <= ny < dimension) or tablero[ny][nx] == "M":
                print("Movimiento invalido")
            else:
                # Descuento de energia solo en casillas nuevas jojo
                if tablero_final[ny][nx] != "J":
                    costo = 1
                    if tablero[ny][nx] == "A":
                        costo = 2
                    energia -= costo
                    
                    if tablero[ny][nx] == "C":
                        checkpoints_logrados += 1
                        print("Checkpoint alcanzado")

                # Actualizacion de la ubicacion del jugador lol
                x_actual = nx
                y_actual = ny
                tablero_final[y_actual][x_actual] = "J"

    # --- RESULTADOS FINALES ---
    # Mensaje final segun la condicion de termino sisi
    if checkpoints_logrados == total_checkpoints:
        print("¡Mapa finalizado!")
    else:
        print("Energia agotada") # ouchet
        
    print("Tablero final:") # juju
    for fila in tablero_final:
        # Construccion de la fila para la salida en pantalla jojo
        linea = ""
        for item in fila:
            linea += item
        print(linea)
        
    print("Energia final:", energia) # sisi
