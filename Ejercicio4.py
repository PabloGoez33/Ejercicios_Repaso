"""Escribir un programa que determine si un número dado es par o impar."""

def main():

    print("\n----------¿Par o impar?----------\n")
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        print(f"El numero {numero} es par.")
    else:
        print(f"El numero {numero} es impar.")

main()