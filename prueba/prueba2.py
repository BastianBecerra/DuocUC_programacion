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
estado = "Bueno"
print("Bienvenido Cientifico.")


while True:
    cadena_adn = input("Ingrese el tipo de cadena de adn. (Recuerte que es A, T, C o G y deben ir juntas de a pares.) para ser almacenada en la lista: ")
    if cadena_adn.lower() == "salir":
        break
    cadena_adn.append(lista_adn) # .append para colocar el elemento creado por el cientifico.
    
for x in "AT" or "TA" or "GC" or "CG" and "-": #intente con range(len()) pero no recorria de buena manera como pensaba
    if x == cadena_adn:
        estado = "Bueno"
        print("Bueno")
    else:
        estado = "Malo"
        print("Malo")
        
        
"""
Intente darle con un diccionario para poder darle un numero de valor a alguno, no resulto ya que no recibia datos, el intento fuee que  con el for en or poderhacer los datos de la cadena que aun asi me da error en el que esta bueno y la verdad no entendi bien el porque no funciono. bueno intente con and y me sigue recibiendo lo que esta malo, pero para ver si podria haber una solucion para saber si estaba bien el correcto
"""

print(list(zip(lista_adn, estado))) #Usamos list con zip para que se vea de mejor manera el codigo pero con un error en el string.