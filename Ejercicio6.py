"""Crear un programa que calcule la suma de los números en una lista dada."""

def main():

    listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    suma = 0

    print("----------Lista numeros----------\n")
    print(listaNumeros)

    for I in range(len(listaNumeros)):
        suma = suma + listaNumeros[I]
    
    print("\n----------Suma de la lista----------\n")
    print(suma)

main()