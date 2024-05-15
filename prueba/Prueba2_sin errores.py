"""
Un grupo de científicos le pasa una lista con secuencias de ADN.

Cada secuencia es un texto que tiene las letras ‘A’ ‘T’ ‘C’ o ‘G’

Las letras siempre deben ir en pares que son AT o TA o CG o GC, todas separadas por un -

Usted debe crear un programa que lea esta lista de cadenas de ADN e indique cuál de estas cadenas es una secuencia válida y cuál no.

Considere que la secuencia solo contendrá letras y el -, estará bien escrita.

ej cadenas:

 AT-CG-GC-GC-AT => BIEN

 AT-TC-TA => MAL

Ejemplo de lista

adn = [

'AT-CG-GG-TA-TA-TT',

'AA-AT-CG-GC-GC-TA-AT',

'AT-TA-GC',

]

resultado:

MALO

MALO

BUENO

"""

lista_adn = ["AT-CG-GG-TA-TA-TT", "AA-AT-CG-GC-GC-TA-AT", "AT-TA-GC"]
pares_validos = {"AT", "TA", "CG", "GC"}
resultado= []
print("Bienvenido Cientifico.")

for cadena in lista_adn:
    es_valida = True
    pares = cadena.split('-')  # Dividir la cadena en pares
    
    for par in pares:
        if par not in pares_validos:
            es_valida = False
            break
    
    if es_valida:
        print("BUENO")
    else:
        print("MALO")

while True:
    cadena_adn = input("Ingrese una cadena de ADN o 'salir' para terminar: ")
    if cadena_adn.lower() == "salir":
        break
    lista_adn.append(cadena_adn) # .append para colocar el elemento creado por el cientifico.
    
for cadena in lista_adn[len(resultado):]:  # Solo verificar nuevas entradas
    es_valida = True
    pares = cadena.split('-')
    
    for par in pares:
        if par not in pares_validos:
            es_valida = False
            break
    
    if es_valida:
        print("BUENO")
    else:
        print("MALO") 
        
"""
Intente darle con un diccionario para poder darle un numero de valor a alguno, no resulto ya que no recibia datos, el intento fuee que  con el for en or poderhacer los datos de la cadena que aun asi me da error en el que esta bueno y la verdad no entendi bien el porque no funciono. bueno intente con and y me sigue recibiendo lo que esta malo, pero para ver si podria haber una solucion para saber si estaba bien el correcto
"""