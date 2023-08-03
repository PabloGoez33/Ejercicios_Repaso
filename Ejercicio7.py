"""Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada."""

def main():

    listaNumero = [3, 5, 10, 21, 47, 59, 22, 100, 85]
    mayor = 0
    menor = 9999

    print("\n----------Lista de numeros----------\n")
    print(listaNumero)

    for I in range(len(listaNumero)):
        if listaNumero[I] > mayor:
            mayor = listaNumero[I]
    
    for I in range(len(listaNumero)):
        if listaNumero[I] < menor:
            menor = listaNumero[I]

    print("\n----------Numero mayor de la lista----------\n")
    print(f"El numero mayor de la lista es el {mayor}")
    print("\n----------Numero menor de la lista----------\n")
    print(f"El numero menor de la lista es el {menor}")

main()