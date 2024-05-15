"""
    while True:
        palabra = input("Ingrese una palabra que desea repetir. (escriba 'salir' para terminar): ")
        if (palabra.lower() == "salir"):
            print("Adios!")
            break
        else:
            print(palabra)
"""
# ej2

"""
sum = 0
cont = 0

while True:
    num = input("ingrese un numero: ")
    if (num == "salir"):
        break
    else:
        sum = int(num) + sum
        cont += 1
print(sum)
print(sum / cont)
""" 
# eje 3
"""
palabra = str(input("Ingrese alguna palabra para contar sus vocales: "))
contador = 0
vocales = "aeiou"

for x in palabra:
    if x in  vocales:
        contador += 1
print("vocales, ", contador)
"""

""""""