import subprocess
import random

def ejecutar_programa(programa, args):
    subprocess.run(['python3', programa] + args)

def modo_manual():
    """Ejecuta en modo manual pidiendo al usuario las cadenas."""
    while True:
        cadena_blanco = input("Ingresa la cadena para el rey blanco (solo 'r' y 'b'): ")
        cadena_negro = input("Ingresa la cadena para el rey negro (solo 'r' y 'b'): ")

        # Contar los caracteres en cadena_blanco
        contador_blanco = 0
        for _ in cadena_blanco:
            contador_blanco += 1
        
        # Contar los caracteres en cadena_negro
        contador_negro = 0
        for _ in cadena_negro:
            contador_negro += 1

        if contador_blanco != contador_negro:
            print("Las cadenas deben ser de la misma longitud. Intenta de nuevo.")
            continue

        if not all(c in 'rb' for c in cadena_blanco + cadena_negro):
            print("Las cadenas solo pueden contener 'r' y 'b'. Intenta de nuevo.")
            continue

        # Ejecutar los programas pasando las cadenas como argumento
        ejecutar_programa('rutaRB.py', [cadena_blanco])
        ejecutar_programa('rutaRN.py', [cadena_negro])

        ejecutar_programa('tablero.py', [])
        ejecutar_programa('redRB.py', [])
        ejecutar_programa('redRN.py', [])

        # Preguntar si desea continuar
        continuar = input("¿Quieres continuar? (s/n): ").lower()
        if continuar != 's':
            break


def modo_automatico():
    """Ejecuta en modo automático generando cadenas aleatorias."""
    while True:
        longitud = random.randint(1, 100)
        cadena_blanco = ''.join(random.choice('rb') for _ in range(longitud))
        cadena_negro = ''.join(random.choice('rb') for _ in range(longitud))

        print(f"Cadenas generadas: Blanco = {cadena_blanco}, Negro = {cadena_negro}")

        # Ejecutar los programas pasando las cadenas como argumento
        ejecutar_programa('rutaRB.py', [cadena_blanco])
        ejecutar_programa('rutaRN.py', [cadena_negro])

        ejecutar_programa('tablero.py', [])
        
        ejecutar_programa('redRB.py', [])
        ejecutar_programa('redRN.py',[])


        # Preguntar si desea continuar
        continuar = input("¿Quieres continuar? (s/n): ").lower()
        if continuar != 's':
            break

def main():
    while True:
        print("Seleccione un modo:")
        print("1. Modo Manual")
        print("2. Modo Automático")
        print("3. Salir")

        eleccion = input("Ingrese su elección (1, 2, o 3): ")

        if eleccion == '1':
            modo_manual()
        elif eleccion == '2':
            modo_automatico()
        elif eleccion == '3':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

