"""Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división."""

def main():

    print("\n----------Ingrese dos numeros----------\n")
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    print("\n----------Operaciones----------\n")
    print("° Suma")
    print(f"\t{numero1} + {numero2} = {numero1 + numero2}")
    print("° Resta")
    print(f"\t{numero1} - {numero2} = {numero1 - numero2}")
    print("° Multiplicacion")
    print(f"\t{numero1} * {numero2} = {numero1 * numero2}")
    print("° Division")
    print(f"\t{numero1} / {numero2} = {round((numero1 / numero2), 2)}")

main()