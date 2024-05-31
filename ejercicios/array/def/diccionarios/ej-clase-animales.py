# SECCION 002 D
# V 4.5
# fecha: 30/05
# hagan los ejercicios

"""
    ✔ Agregar menu para seleccionar:
        ✔ - Mostrar la lista numerada de animales (para poder seleccionar)
            y mostrar detalle del animal 
            ✔ >> solucionar posibles errores en seleccion
        
        ✔ Guardar los animales seleccionados
            
    ✔ Mostrar animales seleccionados
        opciones:
        - limpiar lista
        - ver detalle de un animal
        - quitar item de lista
        
    ✔ Poder 'filtrar' la lista de animales, segun el tipo
        - Agregar a la selccion
        
    ✔ Agregar animales a la lista (deben tener los mismos datos,
        nombre, tipo, peso, color)
        - validar datos

    ✔ Crear Funcion que determine si una seleccion es valida
            El usuario tiene un rango de seleccion, y la funcion retorna True o False
            dependiendo si la seleccion es valida o no

    - Eliminar Animal
            - mostrar la lista
            - seleccionar que cosa eliminar

    - Modificar el dato de un animal

    - Agregar un dato (llave : valor) a un animal           

    

"""
def mostrarLista(lista: list) -> None:
    for i, elemento in enumerate(lista):
        print(i, '=>', elemento)

def mostrarAnimalLista(lista: list) -> None:
    for i, animal in enumerate(lista):
        print(i+1, '. ', animal['nombre'], ' => ', animal['tipo'], sep='')

def mostrarDetalleAnimal(animal: dict) -> None:
    print('-'*10)
    for llave, valor in animal.items():
        print(llave, '=>', valor)

def selOpcion(lista: list, desfase: int = 0) -> int:
    while True:
        sel = input(">> ")
        if sel.isnumeric():
            sel = int(sel) - desfase
            if 0 <= sel < len(lista):
                return sel
        print("Selección inválida. Intente nuevamente.")

def seleccion_valida(rango: int, seleccion: int) -> bool:
    return 0 <= seleccion < rango

def agregarAnimal(lista: list) -> None:
    nombre = input('Ingrese nombre: ')
    tipo = input('Ingrese tipo: ')
    peso = float(input('Ingrese peso: '))
    color = input('Ingrese color: ')
    if nombre and tipo and peso and color:
        lista.append({'nombre': nombre, 'tipo': tipo, 'peso': peso, 'color': color})
    else:
        print("Datos inválidos. Intente nuevamente.")

def filtrarPorTipo(lista: list) -> None:
    lista_filtrada = []
    filtro = input('Ingrese tipo a filtrar: ').lower()
    for animal in lista:
        if animal['tipo'] == filtro:
            lista_filtrada.append(animal)
    mostrarAnimalLista(lista_filtrada)
    print()
    input("Presione Enter para continuar...")  # pausa

def eliminarAnimal(lista: list) -> None:
    mostrarAnimalLista(lista)
    print("Seleccione el animal a eliminar:")
    sel = selOpcion(lista, 1)
    if seleccion_valida(len(lista), sel):
        lista.pop(sel)
        print("Animal eliminado.")
    else:
        print("Selección inválida.")

def modificarAnimal(lista: list) -> None:
    mostrarAnimalLista(lista)
    print("Seleccione el animal a modificar:")
    sel = selOpcion(lista, 1)
    if seleccion_valida(len(lista), sel):
        animal = lista[sel]
        print("Seleccione el dato a modificar:")
        for i, llave in enumerate(animal.keys()):
            print(i+1, '=>', llave)
        sel_dato = selOpcion(list(animal.keys()), 1)
        llave_a_modificar = list(animal.keys())[sel_dato]
        nuevo_valor = input(f'Ingrese el nuevo valor para {llave_a_modificar}: ')
        animal[llave_a_modificar] = nuevo_valor
        print("Animal modificado.")
    else:
        print("Selección inválida.")

def agregarDatoAnimal(lista: list) -> None:
    mostrarAnimalLista(lista)
    print("Seleccione el animal al que desea agregar un dato:")
    sel = selOpcion(lista, 1)
    if seleccion_valida(len(lista), sel):
        animal = lista[sel]
        nueva_llave = input('Ingrese la nueva llave: ')
        nuevo_valor = input('Ingrese el nuevo valor: ')
        animal[nueva_llave] = nuevo_valor
        print("Dato agregado.")
    else:
        print("Selección inválida.")

# Datos iniciales
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

animales_guardados = []

opciones_menu = [
    'salir', #con 0 se sale
    'mostrar lista animales y seleccionar',
    'seleccionar por tipo',
    'agregar animales',
    'mostrar animales guardados',
    'eliminar animal',
    'modificar animal',
    'agregar dato a un animal',
]

# Inicio del programa
while True:  # WHILE MENU
    mostrarLista(opciones_menu)
    sel = selOpcion(opciones_menu)

    if sel == 0:
        break

    if sel == 1:
        mostrarAnimalLista(lista_animales)
        print()
        sel = selOpcion(lista_animales, 1)

        animal_seleccionado = lista_animales[sel]
        mostrarDetalleAnimal(animal_seleccionado)

        if animal_seleccionado not in animales_guardados:
            animales_guardados.append(animal_seleccionado)

        continue

    if sel == 2:
        filtrarPorTipo(lista_animales)
        continue

    if sel == 3:
        agregarAnimal(lista_animales)
        continue

    if sel == 4:
        mostrarAnimalLista(animales_guardados)
        continue

    if sel == 5:
        eliminarAnimal(lista_animales)
        continue

    if sel == 6:
        modificarAnimal(lista_animales)
        continue

    if sel == 7:
        agregarDatoAnimal(lista_animales)
        continue