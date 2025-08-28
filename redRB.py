import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke
import random

def leer_archivo_a_matriz(nombre_archivo):
    # Inicializa una lista para almacenar las filas
    matriz = []
    
    # Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Lee cada línea del archivo
        for linea in archivo:
            # Elimina espacios y separa por '->', luego convierte a enteros
            fila = [int(x.strip()) for x in linea.split('->')]
            # Agrega la fila a la matriz
            matriz.append(fila)
    
    return matriz

def eliminar_repetidos(matriz):
    # Convertir la matriz a un array de numpy con dtype float
    matriz_np = np.zeros_like(matriz, dtype=float)  # Inicializa con ceros
    matriz_np[:] = np.nan  # Llena la matriz con NaN
    
    # Obtener el número de columnas
    num_columnas = matriz_np.shape[1]
    
    # Iterar sobre cada columna
    for col in range(num_columnas):
        elementos_vistos = set()  # Conjunto para almacenar elementos ya vistos
        for fila in range(matriz_np.shape[0]):  # Cambiado para evitar len
            valor = matriz[fila][col]
            if valor in elementos_vistos:
                matriz_np[fila, col] = np.nan  # Reemplaza el valor por NaN
            else:
                elementos_vistos.add(valor)  # Agrega el nuevo elemento al conjunto
                matriz_np[fila, col] = valor  # Guarda el valor en la nueva matriz
    
    return matriz_np

def filtrar_filas_vacias(matriz):
    """Elimina filas que solo contienen NaN."""
    return matriz[~np.all(np.isnan(matriz), axis=1)]

def generar_color_aleatorio():
    """Genera un color aleatorio en formato RGB."""
    return (random.random(), random.random(), random.random())

def graficar_matriz(matriz, rutas):
    # Obtiene las dimensiones de la matriz
    filas, columnas = matriz.shape

    # Configura el tamaño de la figura en función de las dimensiones de la matriz
    plt.figure(figsize=(2 * columnas, 2 * filas))  # Ajusta el tamaño de la figura
    
    # Itera sobre cada celda y coloca el texto correspondiente
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i, j]
            if not np.isnan(valor):  # Solo grafica si el valor no es NaN
                texto = plt.text(j, i, str(int(valor)), ha='center', va='center', fontsize=8, color='black',path_effects=[withStroke(linewidth=7, foreground='white')])

    # Configura el gráfico como una cuadrícula
    plt.xlim(-0.5, columnas - 0.5)
    plt.ylim(filas - 0.5, -0.5)
    plt.xticks(np.arange(columnas), labels=np.arange(1, columnas + 1), rotation=45)  # Rotar etiquetas
    plt.yticks(np.arange(filas), labels=np.arange(1, filas + 1))
    plt.grid(True, which='both', color='black', linestyle='-', linewidth=1, alpha=0.5)

# Dibuja las líneas según las rutas
    for ruta in rutas:
        color = generar_color_aleatorio()  # Genera un color aleatorio solo una vez para cada ruta
        for j in range(np.shape(ruta)[0] - 1):  # Cambiado para evitar len
            y_start = np.where(matriz[:, j] == ruta[j])[0]  # Fila del número de inicio
            y_end = np.where(matriz[:, j + 1] == ruta[j + 1])[0]  # Fila del número de fin
            if y_start.size > 0 and y_end.size > 0:  # Si ambos números están en la matriz
                plt.plot([j, j + 1], [y_start[0], y_end[0]], color=color, linestyle='-', linewidth=2)  # Dibuja la línea


    # Agrega un título
    plt.title('Red Rey Blanco')
    plt.xlabel('')
    plt.ylabel('')

    # Muestra la gráfica
    plt.gca().set_aspect('auto', adjustable='box')
    plt.grid(False)
    plt.show()

# Nombre del archivo de texto
nombre_archivo = 'Rutas/todas_las_rutasRB.txt'

# Llama a la función para leer el archivo y obtener la matriz
matriz_resultante = leer_archivo_a_matriz(nombre_archivo)

# Elimina los repetidos en la matriz
matriz_final = eliminar_repetidos(matriz_resultante)

# Filtra las filas vacías
matriz_final = filtrar_filas_vacias(matriz_final)

# Grafica la matriz final
graficar_matriz(matriz_final, matriz_resultante)
