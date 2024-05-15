"""
Escriba un programa que reciba numeros (pueden ser enteros o decimales) y los guarde en una lista.

El programa deja de recibir numeros cuando el usuario ingresa 0 (no se debe guardar ese numero).

Luego el programa pregunta por un numero, y elimina todos los numeros MENORES al numero ingresado. Luego se muestra la lista.
"""
lista_numeros = []

while True:
    numero = float(input("Ingrese un numero: "))

    if numero == 0:
        break
    lista_numeros.append(numero)

print(lista_numeros)

numero_a_eliminar = float(input("Ingrese un numero: "))

lista_filtrada = [numero for numero in lista_numeros if numero >= numero_a_eliminar]

print(lista_filtrada)