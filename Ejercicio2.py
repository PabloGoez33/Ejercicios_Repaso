"""Escribir una función que calcule el área de un círculo dado su radio."""

def main():

    print("\n----------Area de una circulo----------\n")
    radio = float(input("Ingrese el radio del circulo: "))
    Area = 3.1416 * radio ** 2
    print("\n----------Resultado----------\n")
    print(f"El area del circulo con radio {radio} es: {round(Area,4)}")

main()