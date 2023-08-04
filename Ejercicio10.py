"""Escribir una función que calcule el factorial de un número dado."""

def main():

    factorial = 1

    print("\n----------Factorial de un numero----------\n")
    numero = int(input("Ingrese el numero al cual calcular el factorial: "))

    for I in range(1, numero + 1, 1):
        factorial = factorial * I
    
    print("\n----------Resultado----------\n")
    print(f"El factorial de {numero} es {factorial}")

main()