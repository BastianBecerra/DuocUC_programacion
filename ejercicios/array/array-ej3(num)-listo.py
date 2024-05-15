"""
Cree un programa que reciba numeros positivos, del 0 al 15. el programa se detiene cuando se ingresa un numero negativo. Luego muestre cuanto se repite cada numero.

DESAFIO: Maximo 2 ciclos.
"""
lista_numos = []

for i in range(16):
    lista_numos.append(0)

while True:
    numero = int(input("Ingrese un numero: "))
    if (numero < 0):
        break
    if (numero > 15):
        continue

    lista_numos[numero] += 1

for i in range(len(lista_numos)):
    print(i, '>', lista_numos[i])