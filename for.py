"""
for elemento in "hola":
    print(elemento)
"""

"""
for elemento in range(5): # (2,10,3) hace que se lea del 2 al 5 y termine en 8
    print(elemento)
"""
numero_maximo = 0
numero_minimo = 0
suma = 0
for num in range(10):

    numero = int(input("ingrese numero: "))
    suma += numero

    if (num == 0):
        numero_maximo = numero
        numero_minimo = numero

    if (numero > numero_maximo):
        numero_maximo = numero

    if (numero < numero_minimo):
        numero_minimo = numero


print("Suma:", suma)
print("Promedio:", suma/10)
print("Numero mas alto: ", numero_maximo)
print("Numero mas bajo: ", numero_minimo)

TWOSTONES THEME 


    

