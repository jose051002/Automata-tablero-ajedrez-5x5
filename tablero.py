import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO, ALTO = 1000, 1000
FILAS, COLUMNAS = 5, 5
TAMAÑO_CUADRADO = ANCHO // COLUMNAS
VELOCIDAD_MOVIMIENTO = 3  # Píxeles por cuadro para un movimiento suave

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Configurar la pantalla
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Tablero de Ajedrez 5x5')

# Cargar imágenes
IMAGEN_REY1 = pygame.image.load('Imagenes/RB.png')
IMAGEN_REY2 = pygame.image.load('Imagenes/RN.png')

# Escalar imágenes para ajustarse a los cuadrados
IMAGEN_REY1 = pygame.transform.scale(IMAGEN_REY1, (TAMAÑO_CUADRADO, TAMAÑO_CUADRADO))
IMAGEN_REY2 = pygame.transform.scale(IMAGEN_REY2, (TAMAÑO_CUADRADO, TAMAÑO_CUADRADO))

def dibujar_tablero(ventana, pos_rey1, pos_rey2, rey1_x, rey1_y, rey2_x, rey2_y):
    ventana.fill(NEGRO)
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            if (fila + col) % 2 == 1:
                pygame.draw.rect(ventana, ROJO, (col * TAMAÑO_CUADRADO, fila * TAMAÑO_CUADRADO, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO))

    # Dibujar imágenes en sus posiciones actuales
    ventana.blit(IMAGEN_REY1, (rey1_x, rey1_y))
    ventana.blit(IMAGEN_REY2, (rey2_x, rey2_y))

def cargar_rutas_de_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        rutas = archivo.readlines()
        
        # Verificar si el archivo está vacío
        if not rutas:
            print(f"No hay rutas ganadoras en el archivo: {nombre_archivo}")
            return []  # Retorna una lista vacía si no hay rutas

    rutas = [ruta.strip().split(' -> ') for ruta in rutas]
    rutas = [[int(pos) for pos in ruta] for ruta in rutas]
    return rutas

def encontrar_ruta_alternativa(rutas, pasos_actuales, pos_rey2):
    # Busca una ruta que coincida con los pasos actuales y que no colisione con la posición de rey2
    for ruta in rutas:
        if ruta[:len(pasos_actuales)] == pasos_actuales and (len(ruta) > len(pasos_actuales) and ruta[len(pasos_actuales)] != pos_rey2):
            return ruta
    return None

def mover_suavemente(rey_x, rey_y, objetivo_x, objetivo_y):
    direccion_x = objetivo_x - rey_x
    direccion_y = objetivo_y - rey_y
    distancia = (direccion_x ** 2 + direccion_y ** 2) ** 0.5

    if distancia == 0:
        return rey_x, rey_y

    mover_x = (direccion_x / distancia) * VELOCIDAD_MOVIMIENTO
    mover_y = (direccion_y / distancia) * VELOCIDAD_MOVIMIENTO

    if abs(mover_x) > abs(direccion_x):
        mover_x = direccion_x
    if abs(mover_y) > abs(direccion_y):
        mover_y = direccion_y

    return rey_x + mover_x, rey_y + mover_y

def main():
    reloj = pygame.time.Clock()
    ejecutar = True

    # Cargar rutas desde archivos
    rutas_rey1 = cargar_rutas_de_archivo('Rutas/rutas_ganadorasRB.txt')
    rutas_rey2 = cargar_rutas_de_archivo('Rutas/rutas_ganadorasRN.txt')

    # Verificar si hay rutas disponibles
    if not rutas_rey1 or not rutas_rey2:
        print("No se pueden iniciar las partidas debido a rutas ganadoras faltantes.")
        pygame.quit()
        sys.exit()

    ruta_seleccionada1 = random.choice(rutas_rey1)
    ruta_seleccionada2 = random.choice(rutas_rey2)

    paso1 = 0
    paso2 = 0

    pos_rey1 = ruta_seleccionada1[paso1]
    pos_rey2 = ruta_seleccionada2[paso2]

    fila_rey1, col_rey1 = divmod(pos_rey1 - 1, COLUMNAS)
    rey1_x, rey1_y = col_rey1 * TAMAÑO_CUADRADO, fila_rey1 * TAMAÑO_CUADRADO

    fila_rey2, col_rey2 = divmod(pos_rey2 - 1, COLUMNAS)
    rey2_x, rey2_y = col_rey2 * TAMAÑO_CUADRADO, fila_rey2 * TAMAÑO_CUADRADO

    turno_actual = random.choice([1, 2])

    pygame.display.flip() #Actualiza la pantalla

    while ejecutar:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False

        if turno_actual == 1:
            if paso1 < len(ruta_seleccionada1) - 1:
                siguiente_pos1 = ruta_seleccionada1[paso1 + 1]

                # Si la siguiente posición de rey1 es la actual de rey2, buscar una ruta alternativa
                if siguiente_pos1 == pos_rey2:
                    ruta_alt = encontrar_ruta_alternativa(rutas_rey1, ruta_seleccionada1[:paso1 + 1], pos_rey2)
                    if ruta_alt:
                        ruta_seleccionada1 = ruta_alt
                    else:
                        turno_actual = 2  # Omitir turno si no hay ruta alternativa
                        continue

                siguiente_fila1, siguiente_col1 = divmod(siguiente_pos1 - 1, COLUMNAS)
                objetivo_x1, objetivo_y1 = siguiente_col1 * TAMAÑO_CUADRADO, siguiente_fila1 * TAMAÑO_CUADRADO

                rey1_x, rey1_y = mover_suavemente(rey1_x, rey1_y, objetivo_x1, objetivo_y1)

                if abs(rey1_x - objetivo_x1) < VELOCIDAD_MOVIMIENTO and abs(rey1_y - objetivo_y1) < VELOCIDAD_MOVIMIENTO:
                    paso1 += 1
                    pos_rey1 = siguiente_pos1
                    turno_actual = 2
                    if paso1 == len(ruta_seleccionada1) - 1:
                        print('El Rey Blanco ha terminado su recorrido.')
                        print('Ruta ganadora:', ruta_seleccionada1)
                        ejecutar = False

        elif turno_actual == 2:
            if paso2 < len(ruta_seleccionada2) - 1:
                siguiente_pos2 = ruta_seleccionada2[paso2 + 1]

                # Si la siguiente posición de rey2 es la actual de rey1, buscar una ruta alternativa
                if siguiente_pos2 == pos_rey1:
                    ruta_alt = encontrar_ruta_alternativa(rutas_rey2, ruta_seleccionada2[:paso2 + 1], pos_rey1)
                    if ruta_alt:
                        ruta_seleccionada2 = ruta_alt
                    else:
                        turno_actual = 1  # Omitir turno si no hay ruta alternativa
                        continue

                siguiente_fila2, siguiente_col2 = divmod(siguiente_pos2 - 1, COLUMNAS)
                objetivo_x2, objetivo_y2 = siguiente_col2 * TAMAÑO_CUADRADO, siguiente_fila2 * TAMAÑO_CUADRADO

                rey2_x, rey2_y = mover_suavemente(rey2_x, rey2_y, objetivo_x2, objetivo_y2)

                if abs(rey2_x - objetivo_x2) < VELOCIDAD_MOVIMIENTO and abs(rey2_y - objetivo_y2) < VELOCIDAD_MOVIMIENTO:
                    paso2 += 1
                    pos_rey2 = siguiente_pos2
                    turno_actual = 1
                    if paso2 == len(ruta_seleccionada2) - 1:
                        print('El Rey Negro ha terminado su recorrido.')
                        print('Ruta ganadora:', ruta_seleccionada2)
                        ejecutar = False

        dibujar_tablero(VENTANA, pos_rey1, pos_rey2, rey1_x, rey1_y, rey2_x, rey2_y)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
