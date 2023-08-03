"""Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla."""

def main():

    print("\n-------------Ingrese datos-------------\n")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    print("\n-------------Resultado-------------\n")
    print(f"Hola {nombre}, su edad es {edad}")

main()