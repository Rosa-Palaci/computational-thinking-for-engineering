#Actividad Evaluable - Programas que utilizan funciones
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 2

# INSTRUCCIONES:
# Define una función que reciba el lado de un cubo y calcule su área. 
# Utiliza esa función para calcular el área de tres cubos distintos 
# (el lado de cada cubo lo proporciona el usuario).

import math

def areaCubo(lado):
    '''Area total del cubo es = Area de una cara x 6'''
    if lado == 0:
        return math.nan
    else:
        return 6* lado * lado


for repetir in range(3):
    lado = float(input('Digite el valor del lado: '))
    area = areaCubo(lado)
    print(f'El área del cubo es: {area} ') 