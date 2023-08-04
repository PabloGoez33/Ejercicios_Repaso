"""Crear un programa que genere una matriz de números y la imprima en pantalla."""

def main():

    import random

    Matriz = []

    """Ingresar datos."""

    print("\n---------Inicializar matriz----------\n")
    filas = int(input("Ingrese el numero de filas de la matriz: "))
    columnas = int(input("Ingrese el numero de columnas de la matriz: "))

    """Inicializar matriz."""

    for F in range(filas):
        Matriz.append([0] * columnas)
    
    print("\n---------Matriz generada----------\n")
    print(Matriz)

    """Llenar matriz."""

    for F in range(filas):
        for C in range(columnas):
            Matriz[F][C] = random.randint(0,100)
    
    """Imprimir matriz"""

    print("\n---------Matriz llena con numeros aleatorios----------\n")
    print(Matriz)

main()