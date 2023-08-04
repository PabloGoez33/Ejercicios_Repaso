"""Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no."""

def main():

    igual = 0
    aux = 0

    print("\n----------Ingrese palabra----------\n")
    palabra = input("Ingrese una palabra que desee evaluar: ")

    for I in reversed(range(0, len(palabra))):
        if palabra[I].lower() == palabra[aux].lower():
            igual = igual + 1
        aux = aux + 1
    
    print("\n----------Resultado----------\n")
    if len(palabra) == igual:
        print("La palabra es palídromo.")
    else:
        print("La palabra no es palíndromo")

main()