# SECCION 002 D
# V 1
# fecha: 28/05
# hagan los ejercicios

"""
    ✔  1. Mostrar la lista numerada de animales (para poder seleccionar) 
         1.5. solucionar posibles errores en seleccion
    2. Poder 'filtrar' la lista de animales, segun el tipo
    3. Agregar animales a la lista (deben tener los mismos datos,
    nombre, tipo, peso, color)
"""

lista_animales = [
    {
        'nombre': 'pepito',
        'tipo' : 'gato',
        'peso' : 7.2, 
        'color' : 'naranjo',
    },
    {
        'nombre': 'jaimico',
        'tipo' : 'mandril',
        'peso' : 20.2, 
        'color' : 'plomo',
    },
    {
        'nombre': 'soy la comadreja',
        'tipo' : 'comadreja',
        'peso' : 7.2, 
        'color' : 'rojo',
    },
    {
        'nombre': 'mojojojo',
        'tipo' : 'mono',
        'peso' : 25.3, 
        'color' : 'verde',
    },
    {
        'nombre': 'mordecai',
        'tipo' : 'azulejo',
        'peso' : 2.2, 
        'color' : 'azul',
    },
    {
        'nombre': 'skips',
        'tipo' : 'yeti',
        'peso' : 200, 
        'color' : 'blanco',
    },
    {
        'nombre': 'rigby',
        'tipo' : 'mapache',
        'peso' : 8, 
        'color' : 'cafe',
    },
    {
        'nombre': 'pedro',
        'tipo' : 'mapache',
        'peso' : 5, 
        'color' : 'negro',
    },
    {
        'nombre': 'panxito',
        'tipo' : 'conejo',
        'peso' : 3, 
        'color' : 'verde',
    },
    {
        'nombre': 'panxote',
        'tipo' : 'conejo',
        'peso' : 10, 
        'color' : 'azul',
    },
]


# 1. Mostrar la lista numerada de animales (para poder seleccionar)

for i in range(len(lista_animales)):
    print(f"{i + 1}. {lista_animales[i]['nombre']}")

# 2. Poder 'filtrar' la lista de animales, segun el tipo

tipo_buscado = input("Ingrese el tipo de animal que desea buscar: ")

for animal in lista_animales:
    if animal['tipo'] == tipo_buscado:
        print(animal['nombre'])

# 3. Agregar animales a la lista (deben tener los mismos datos, nombre, tipo, peso, color)

nombre = input("Ingrese el nombre del animal: ")
tipo = input("Ingrese el tipo del animal: ")
peso = float(input("Ingrese el peso del animal: "))
color = input("Ingrese el color del animal: ")

nuevo_animal = {
    'nombre': nombre,
    'tipo' : tipo,
    'peso' : peso,
    'color' : color,
}

lista_animales.append(nuevo_animal)

for x in range(len(lista_animales)):
    print(f"{x + 1}. {lista_animales[x]['nombre']}, {lista_animales[x]['tipo']}, {lista_animales[x]['peso']}, {lista_animales[x]['color']}")

# Solcion en clases.

for l, animal in enumerate(lista_animales):
    print(l+1,'. ', animal['nombre'], ' / ', animal['tipo'], sep='')

print()

sel = int(input("seleccione animal: "))-1

animal_seleccionado = lista_animales[sel]

print('-'*10)

for llave in animal_seleccionado.keys():
    print(llave,'=>',animal_seleccionado[llave])

tipo_buscado = input("Ingrese el tipo de animal que desea buscar: ")

for animal in lista_animales:
    if animal['tipo'] == tipo_buscado:
        print(
            animal['nombre'],
            '=>',
            animal['tipo']
        )