"""
Realize un algoritmo que reciba un texto e indique cuantas vocales (contando cada una por separado) hay en el texto.

DESAFIO. Usar 1 solo ciclo
"""
texto = input("Ingrese un texto: ")
vocales = ["a", "e", "i", "o", "u"]
contador = 0

for vocales in texto:
    if vocales == "a" or vocales == "e" or vocales == "i" or vocales == "o" or vocales == "u":
        contador += 1
    
print(f"hay este numero {contador} de vocales en el texto")
