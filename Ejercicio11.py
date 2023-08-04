"""Crear un programa que genere una lista de números pares entre 1 y 100."""

def main():

    listaNumeros = []

    for I in range(101):
        if I % 2 == 0:
            listaNumeros.append(I)

    print("\n----------Lista de numeros pares----------\n")    
    print(listaNumeros)

main()