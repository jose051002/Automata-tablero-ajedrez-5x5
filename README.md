# Autómata Tablero 5x5

Implementación un **autómata** sobre un tablero de ajedrez de 5x5, simulando movimientos y rutas para dos piezas en movimientos de una casilla en una casilla. 
El objetivo de cada pieza es llegar a la esquina inferior contraria (Casillas 21 y 25).
Incluye visualización de rutas, reporte y manejo de sprites para representar el estado del tablero.

---

## Estructura del proyecto

- `main.py` → Archivo principal para ejecutar la simulación.  
- `tablero.py` → Lógica y representación del tablero 5x5.  
- `redRB.py`, `redRN.py` → Implementación para visualizar las redes de las rutas de las de piezas (Rey Blanco y Rey Negro).  
- `rutaRB.py`, `rutaRN.py` → Cálculo de rutas para cada pieza.  
- `requirements.txt` → Dependencias necesarias para ejecutar el proyecto.  
- `Reporte_Tablero.pdf` → Reporte sobre la implementación, muestra los resultados y el funcionamiento .  
- `Imagenes/` → Imágenes de las piezas (`RB.png`, `RN.png`).  
- `Rutas/` → Carpeta para almacenar rutas generadas.  

---

## Requisitos

Instalar las dependencias con:

```bash
pip install -r requirements.txt
```
## Uso  

### Programa principal en python 
  ```bash
   python main.cpp 
  ```
### Salida
Reporte y Resultados.pdf contiene un reporte escolar mostrando la explicación y funcionamiento del programa.
Funcionamiento.mp4 muestra un video de la funcionalidad
