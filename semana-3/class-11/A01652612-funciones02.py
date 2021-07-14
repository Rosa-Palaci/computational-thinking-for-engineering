#Actividad Evaluable - Programas que utilizan funciones
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 2
'''
INSTRUCCIONES:
Define una función que reciba el lado de un cubo y calcule su área. 
Utiliza esa función para calcular el área de tres cubos distintos 
(el lado de cada cubo lo proporciona el usuario).
'''
import math

def ecuacionCuad(a, b, c):

    if b**2 - 4 *(a*c) < 0:
        x1 = math.nan
        x2 = math.nan
    else: 
        x1 = (-b + math.sqrt (b**2 - 4 * a*c)) / (2*a)
        x2 = (-b - math.sqrt (b**2 - 4 * a*c)) / (2*a)
    
    return x1, x2

a = int(input('Introduce a: '))
b = int(input('Introduce b: '))
c = int(input('Introduce c: '))

x1, x2 = ecuacionCuad(a, b, c)
print(f'Las soluciones son: x1={x1} x2={x2} ')

'''
Introduce a - 1
Introduce b - 8
introduce c - 15
Las soluciones son x1= 3.0 x2=-5.0
'''