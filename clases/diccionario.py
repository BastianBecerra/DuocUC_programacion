"""
lista comun
"""
lista = [
    "pedrito", "pepito", "patroclo"
]

tipo = [
    "gato", "mapache", "caballo"
]

#for i in range(len(lista)):
#    print(lista[i], tipo[i]

animales = [
    ["pepito", "gato"],
    ["pablito", "cacatua"],
    ["caballo", "patroclo"],
]

for animal in animales:
    nombre = animal[0]
    tipo = animal[1]
   # print(nombre, "=>", tipo)

"""
Diccionario, es como una lista pero entramos a un indice numerico
"""

datos_pedrito = {
    "nombre": "Pedrito VIII de Torrealba",
    "edad": 4,
    "tipo": "mapache",
    "comida_fav": ["zanahorias", "papas", "pepino"]
}

#   print(datos_pedrito["nombre"], "=>", datos_pedrito["tipo"])
"""
Con .keys() nos da los datos de las keys
Con .values() nos da los datos despus de las keys
"""

#for key in datos_pedrito:
#   print(key, "=>", datos_pedrito[key])

#print(len(datos_pedrito))

datos_pedrito["nombre_resumido"] = 'Pepito'
datos_pedrito['color'] = 'cafecito'

"""
Igual se puede hacer con input
"""
"""
llave = input('llave: ' ).lower()
valor = input('valor: ' ).lower()
datos_pedrito[llave] = valor
"""

#for key in datos_pedrito:
#   print(key, "=>", datos_pedrito[key])

"""
En los diccionarios con ,update() podemos actualizar para tener un diccionario vacio y un diccionario al cual ya tenga los valores.

.pop() debe recibir si o si una llave si no se cae el programa. ESTO SOLO EN LOS DICCIONARIOS.
"""

#for comida in datos_pedrito["comida_fav"]:
#
#     print(comida)

"""El Diccionario es un contenedor de datos"""

menu = [
    {
        'nombre': 'Cazuela',
        'precio': 4500,
        'veg': False
    },
    {
        'nombre': 'Churrasco',
        'precio': 3500,
        'veg': True
    },
    {
        'nombre': 'Papas Frittas',
        'precio': 1500,
        'veg': False
    }
]

for item in menu:
    print(item['nombre'])
