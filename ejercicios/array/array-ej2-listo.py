"""
Cree un programa que reciba numeros y los guarde en una lista. Luego, debe mostrar el numero más grande de la lista.
"""

lista_numeros = []
num_mayor = 0

while True:
    numeros = input("Ingrese un numero: ")
    if (numeros.lower() == "salir"):
        print("Adios!")
        break
    lista_numeros.append(int(numeros))
for numero in lista_numeros:
    if (numero > num_mayor):
        num_mayor = numero


print(num_mayor, lista_numeros)