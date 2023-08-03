"""Crear una función que convierta grados Fahrenheit a grados Celsius."""

def main():

    print("\n----------Fahrenheit a Celsius----------\n")
    fahrenheit = float(input("Ingrese la temperatura(Fahrenheit): "))

    celsius = (fahrenheit - 32) * (5/9)
    print("\n----------Resultado----------\n")
    print(f"Los {fahrenheit} grados fahrenheit equivalen a {round(celsius, 5)} grados celsius.")


main()