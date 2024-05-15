# Arreglos o Listas
"""Agrupar datos bajo un solo nombre"""

lista = []

miLista = [ 1, 2, 3 ,4 ,5 ,6 ]

# print( miLista[2] )

"""La lista en negativo va de atras hacia adelante -1 mostraria el 6 y -2 mostraria el 5"""

miLista2 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ]

# print( miLista2[1:4] )

"""Para modificar una lista existen tres metodos  append / insert / pop"""
# append agrega al final de la lista y mantiene orden 
""" 
miLista.append(7)
print(miLista) 
"""
# Inserta donde uno quiera el numero, con especificaciones (2, 48)
"""
miLista.insert(2, 48)
print(miLista)
"""
# Pop para sacar cosas de la lista
"""
print(miLista)
print()
"""
# miLista.pop()
"""Colocando un numero puedo elegir el que sera sacado de la lista"""
"""
comida = miLista.pop()

print(miLista)
print(comida)
"""

"""Ej1"""
"""
lista_relleno = []

while True:
    palabra = input("ingrese una palabra para la lista: ").lower()
    if palabra == "salir":
        break
    else:
        lista_relleno.append(palabra)

# print(lista_relleno)
"""

"""EJ 2"""

numero_max = 0
lista_numeros = []

while True:
    numero = str(input("Escriba un numero para la lista, escriba `salir` para terminar y ver la lista: "))

    if numero.lower() == "salir":
        break

    if numero.isdigit() == False:
        continue

    else:
        lista_numeros.append(int(numero))

# El for es para ingresar a la lista asi poder ver la lista y con la variable i para recorrer la lista y asi se almacena el nuevo numero.

for i in lista_numeros:

    if (i  > numero_max):
        numero_max = i

print(lista_numeros)
print("Numero mayor fue: ", numero_max)
