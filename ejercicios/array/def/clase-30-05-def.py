def imprimirLista ( lista: list, nombre:str='LISTA') -> None:
    for elemento in lista:
        print(elemento)

def promedio (Lista:list) -> float:
    suma = 0
    for i in lista:
        suma += i
    prom = suma / len(lista)
    return prom

lista = [1,2,3,4,5,6,7,8,9,10]
lista_num = [123, 432, 546, 4, 3245]

p = promedio(lista)

print(p)
#   imprimirLista(lista)
#   imprimirLista(lista_num, 'lista 8')