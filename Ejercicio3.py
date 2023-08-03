""" Crear un programa que genere una lista de números aleatorios y los imprima en pantalla."""

def main():

    import random

    listaNumeros = []
    for I in range(10):
        listaNumeros.append(random.randint(0, 10))
    print("\n----------Lista de numeros aleatorios----------\n")
    print(listaNumeros)

main()