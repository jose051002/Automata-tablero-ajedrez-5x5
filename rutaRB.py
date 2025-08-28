import sys

def generar_movimientos(tablero, secuencia, posicion_inicial=1):
    movimientos = []

    # Definir el color que corresponde a 'r' y 'b'
    colores = {'r': 'rojo', 'b': 'negro'}

    # Función recursiva para generar las combinaciones de movimientos
    def explorar(posicion_actual, secuencia_restante, ruta):
        if not secuencia_restante:  # Si la secuencia está vacía, guardar la ruta
            movimientos.append(ruta)
            return

        color_deseado = secuencia_restante[0]  # Color que queremos respetar en este paso
        adyacentes = tablero[posicion_actual]  # Posiciones adyacentes de la actual

        # Verifica si el color deseado está en el diccionario
        if color_deseado not in adyacentes:
            return  # Si el color no está, terminar la búsqueda

        # Explorar cada posición adyacente
        for adyacente in adyacentes[color_deseado]:
            # Si el color coincide, explorar más desde esta posición
            explorar(adyacente, secuencia_restante[1:], ruta + [adyacente])

    # Iniciar la búsqueda desde la posición inicial
    explorar(posicion_inicial, secuencia, [posicion_inicial])

    return movimientos


# Definir posiciones adyacentes (por color) para el tablero de ajedrez de 5x5
tablero = {
    1: {'r': [2, 6], 'b': [7]},
    2: {'r': [6, 8], 'b': [1, 3, 7]},
    3: {'r': [2, 4, 8], 'b': [7, 9]},
    4: {'r': [8, 10], 'b': [3, 5, 9]},
    5: {'r': [4, 10], 'b': [9]},
    6: {'r': [2, 12], 'b': [1, 7, 11]},
    7: {'r': [2, 6, 8, 12], 'b': [1, 3, 11, 13]},
    8: {'r': [2, 4, 12, 14], 'b': [3, 7, 9, 13]},
    9: {'r': [4, 8, 10, 14], 'b': [3, 5, 13, 15]},
    10: {'r': [4, 14], 'b': [5, 9, 15]},
    11: {'r': [6, 12, 16], 'b': [7, 17]},
    12: {'r': [6, 8, 16, 18], 'b': [7, 11, 13, 17]},
    13: {'r': [8, 12, 14, 18], 'b': [7, 9, 17, 19]},
    14: {'r': [8, 10, 18, 20], 'b': [9, 13, 15, 19]},
    15: {'r': [10, 14, 20], 'b': [9, 19]},
    16: {'r': [12, 22], 'b': [11, 17, 21]},
    17: {'r': [12, 16, 18, 22], 'b': [11, 13, 21, 23]},
    18: {'r': [12, 14, 22, 24], 'b': [13, 17, 19, 23]},
    19: {'r': [14, 18, 20, 24], 'b': [13, 15, 23, 25]},
    20: {'r': [14, 24], 'b': [15, 19, 25]},
    21: {'r': [16, 22], 'b': [17]},
    22: {'r': [16, 18], 'b': [17, 21, 23]},
    23: {'r': [18, 22, 24], 'b': [17, 19]},
    24: {'r': [18, 20], 'b': [19, 23, 25]},
    25: {'r': [20, 24], 'b': [19]}
}

# Función para guardar las rutas en los archivos correspondientes
def guardar_rutas(movimientos):
    with open("Rutas/todas_las_rutasRB.txt", "w") as todas, open("Rutas/rutas_ganadorasRB.txt", "w") as ganadoras, open("Rutas/rutas_perdedorasRB.txt", "w") as perdedoras:
        for movimiento in movimientos:
            ruta_str = " -> ".join(map(str, movimiento))  # Convertir la ruta en una cadena legible
            todas.write(ruta_str + "\n")  # Guardar todas las rutas

            if movimiento[-1] == 25:
                ganadoras.write(ruta_str + "\n")  # Guardar rutas ganadoras
            else:
                perdedoras.write(ruta_str + "\n")  # Guardar rutas perdedoras

# Verificar que se proporcionó un argumento en la terminal
if len(sys.argv) != 2:
    print("Uso: python nombre_del_script.py <secuencia_de_colores>")
    sys.exit(1)

# Obtener la secuencia de colores del argumento
secuencia = sys.argv[1].strip().lower()

# Validar la secuencia de colores
if not all(c in ['r', 'b'] for c in secuencia):
    print("La secuencia solo debe contener 'r' para rojo y 'b' para negro.")
    sys.exit(1)

# Generar los movimientos posibles
movimientos_posibles = generar_movimientos(tablero, secuencia)

# Guardar las rutas en archivos
guardar_rutas(movimientos_posibles)

# Mostrar los movimientos posibles
if movimientos_posibles:
    print("Calculando Rutas Rey Blanco")
    #for i, movimiento in enumerate(movimientos_posibles, 1):
        #print(f"Camino {i}: {movimiento}")
else:
    print("No hay caminos posibles que respeten la secuencia de colores.")
