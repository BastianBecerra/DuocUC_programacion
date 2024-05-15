print(" Bienvenido a la fabrica de uvas Mi Pancita!!    ")
#   Variables 
peso = int(input("Ingrese el Peso: ")) # Con float hubiera quedado mejor
radio = int(input("Ingrese el radio: "))    # Con float hubiera quedado mejor
densidad = int(input("Ingrese la densidad: "))  # Con float hubiera quedado mejor
cantidad_gusanos = int(input("Ingrese la cantidad de gusanos: "))   # Con float hubiera quedado mejor
color_de_uva = str(input("Ingrese el color de la uva que desee: ")).lower()

puedes_sacar_la_uva = "NO" # Variable que condiciona a que por defecto no puedan sacar uvas

"""
    Uva morada
        peso: 6 o mas / >= 6
        radio: distinto de 8 / != 8
        densidad: igual o menos a 10 / <= 10
        cantidad de gusanos: igual a 0
"""
if (color_de_uva == "morada") and (peso >= 6) and (radio != 8) and (densidad <= 10) and (cantidad_gusanos == 0): # Error en la densidad era asi >=
    puedes_sacar_la_uva = "SI"

"""
    Uva verde
        peso: cualquiera - no es necesario escribirlo
        radio: almenos 12 / <= 12
        densidad: entre 12 y 18 / (densidad == 12) and (densidad <= 18)
        cantidad de gusanos: no importa - no es necesario
"""
if (color_de_uva == "verde") and (radio <= 12) and ( 12 <= densidad <= 18): # Error en radio >=
    puedes_sacar_la_uva = "SI"
"""
    Uva Roja
        peso: que sea par
        radio: exactamente 16 / == 16
        densidad: 12 o mas  / <= 12
        cantidad de gusanos: igual a 0
"""
if (color_de_uva == "roja") and (peso % 2 == 0) and (radio == 16) and (densidad <= 12) and (cantidad_gusanos == 0): # Error >= en densidad
        puedes_sacar_la_uva = "SI"
    
"""
    Uva Celeste
        peso: igual o almenos 13 / <= 13 
        radio: todo excepto 10 / != 10
        densidad: menos de  3 / <= 3
        cantidad de gusanos: no  mas a 3 / <= 3
"""
if (color_de_uva == "celeste") and (peso <= 13) and (radio != 10) and (densidad < 3) and (cantidad_gusanos <= 3): # Error peso >= 13  radio bien, error en gusanos 3 <= cantidad_gusanos <= 5
     puedes_sacar_la_uva = "Si"

"""
Errores de comprension mas que nada, bien el codigo, pero mas comprension, el float no era tan necesario lo otro es mas con errores de comprension
"""

    




print(f"La uva de color {color_de_uva} {puedes_sacar_la_uva} puede ser sacada") # El .format o f al principio de las comillas hace que se pueda leer las variables como string sin tener que usar la suma de + string + ahorrando codigo.