"""
Cree un programa que reciba palabras y las guarde en una lista. Si el usuario ingresa 'salir'. Se detiene el ingreso de palabras y se muestra la lista en pantalla. Salir no se tiene que guardar en la lista.
"""

palabras = []

while True:
    palabra = input("Ingrese una palabra que desea repetir.(escriba 'salir' para terminar): ")
    if (palabra.lower() == "salir"):
        print("Adios!")
        break
    palabras.append(palabra)


print(palabras)