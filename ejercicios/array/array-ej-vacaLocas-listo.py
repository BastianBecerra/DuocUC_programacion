"""
    En un campo hay muchas vacas con nombres distintos.
    El granjero ha registrado todos los nombre de las vacas en una lista.
    Su trabajo es crear un programa que reciba una letra y muestre todos los nombres que tengan esa letra.
    El programa debe mostrar las vacas de forma enumerada, ya que el granjero luego puede seleccionar (usando el numero) una vaca.
    Cuando el granjero selecciona la vaca, sale un mensaje que dice '<nombre de vaca> ha sido seleccionada'
"""

nombres_vacas = [
    "Juan Daniel",
    "Achraf",
    "Jessica",
    "Bernardo",
    "Rosario",
    "Alexis",
    "Ariana",
    "Sacramento",
    "Patrocinio",
    "Patroclo",
    "Viviana",
    "Aroa",
    "Remedios",
    "Luis",
    "David",
    "Urko",
    "Rosa",
    "Isabel",
    "Gael",
    "Josep",
    "Oriol",
    "Maria",
    "Josefa",
    "Elsa",
]

lista_nueva_vacas = []

letra = str(input("Ingrese una letra: ")).lower()

for nombre in nombres_vacas:
    if letra in nombre:
        lista_nueva_vacas.append(nombre)

for i in range(len(lista_nueva_vacas)):
    print(f"{i + 1} - {lista_nueva_vacas[i]}")
    if letra in nombre:
        print(f"{lista_nueva_vacas[i]} ha sido seleccionada")

numero = int(input("Ingrese el numero de la vaca que desea seleccionar: "))

print(f"{lista_nueva_vacas[numero - 1]} ha sido seleccionada")
