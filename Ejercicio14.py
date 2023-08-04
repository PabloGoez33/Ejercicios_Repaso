"""Escribir una función que calcule la media aritmética de una lista de números."""

def main():

    import random

    listaNumeros = []
    media = 0
    suma = 0

    print("\n----------Configuracion lista----------\n")
    tam = int(input("Ingrese el tamaño de la lista: "))

    """Llenar lista con numeros aleatorios"""

    for I in range(tam):
        listaNumeros.append(random.randint(0,10))
    
    print("\n----------Lista de numeros----------\n")
    print(f"{listaNumeros}\n")

    """Calcular media aritmetica"""

    for I in range(len(listaNumeros)):
        suma = suma + listaNumeros[I]
    media = suma / len(listaNumeros)

    print("\n----------Resultado----------\n")
    print(f"La media aritmetica dela lista es {round(media, 2)}")

main()