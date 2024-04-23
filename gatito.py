# Python 3
def dibujar_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def movimiento_jugador(tablero):
    while True:
        fila = int(input("Ingresa la fila (0-2): "))
        col = int(input("Ingresa la columna (0-2): "))
        if tablero[fila][col] == ' ':
            tablero[fila][col] = 'X'
            break
        else:
            print("Esa posición ya está ocupada. Intenta de nuevo.")

def verificar_ganador(tablero):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return True
    return False
# Python 3
def minimax(tablero, profundidad, es_maximizador):
    if profundidad == 0 or verificar_ganador(tablero):
        if verificar_ganador(tablero):
            return -1 if es_maximizador else 1
        return 0
    if es_maximizador:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'O'
                    eval = minimax(tablero, profundidad - 1, False)
                    tablero[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'X'
                    eval = minimax(tablero, profundidad - 1, True)
                    tablero[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def movimiento_ia(tablero):
    mejor_eval = float('-inf')
    mejor_movimiento = None
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = 'O'
                eval = minimax(tablero, 2, False)
                tablero[i][j] = ' '
                if eval > mejor_eval:
                    mejor_eval = eval
                    mejor_movimiento = (i, j)
    tablero[mejor_movimiento[0]][mejor_movimiento[1]] = 'O'
    
def main():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        dibujar_tablero(tablero)
        movimiento_jugador(tablero)
        if verificar_ganador(tablero):
            print("¡El jugador ha ganado!")
            break
        movimiento_ia(tablero)
        if verificar_ganador(tablero):
            print("¡La IA ha ganado!")
            break

if __name__ == "__main__":
    main()