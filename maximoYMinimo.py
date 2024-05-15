"""
Maximo y Minimo

Cree un programa que reciba enteros (pueden ser negativos o positivos). El programa deja de recibir numeros cuando se ingresa 0.

Al final el programa imprime cual fue el numero más grande ingresado y cual fue el más pequeño.

Extra Considere que en la entrada pueden haber strings (por error). Evite que el programa falle en ese caso.

"""
numero_maximo = -float("inf")
numero_minimo = float("inf")

while (True):
    numero_ingresado = input("Ingrese numero (Con el 0 terminara el programa): ")
    try:
        numero = int(numero_ingresado)
        if (numero == 0):
            break
        if (numero > numero_maximo):
            numero_maximo = numero

        if (numero < numero_minimo):
            numero_minimo = numero
    except ValueError:
        print("Pofavor solo ingresar numeros enteros, pueden ser negativos o positivos: ")

if numero_maximo == -float('inf') or numero_minimo == float('inf'):
    print("No se ingresaron números válidos.")
else:
    print(f"El número más grande ingresado fue: {numero_maximo}")
    print(f"El número más pequeño ingresado fue: {numero_minimo}")