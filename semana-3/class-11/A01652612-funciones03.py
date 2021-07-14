#Actividad Evaluable - Programas que utilizan funciones
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 

'''
INSTRUCCIONES:
Define una función que reciba los coeficientes a, b y c de una ecuación cuadrática 
de la forma ax^2+bx+c=0 y deberá regresar las soluciones x1yx2. 

**(NOTA: si la ecuación tiene soluciones complejas, x1yx2
deberán regresar el valor NaN (not a number), representado en Python como math.nan.)**

Utiliza esa función para calcular la solución de dos ecuaciones cuadráticas distintas 
(los coeficientes de ambas ecuaciones son proporcionadas por el usuario).
'''
import math

print('\nIngresa valores para los coeficientes de a, b y c\n \nPara una ecuación cuadrática de la forma:\n ax^2 + bx + c = 0\n')

def ecuacionCuadratica(a, b, c):

    if b**2 - 4 *(a*c) < 0:
        x1 = math.nan
        x2 = math.nan
    else: 
        x1 = (-b + math.sqrt (b**2 - 4 * a*c)) / (2*a)
        x2 = (-b - math.sqrt (b**2 - 4 * a*c)) / (2*a)
    
    return x1, x2

a = int(input('Digite valor de a: '))
b = int(input('Digite valor de b: '))
c = int(input('Digite valor de c: '))
print(f'\n{a}x^2 + {b}x + {c} = 0\n')

x1, x2 = ecuacionCuadratica(a, b, c)

print(f'Las soluciones para\n x1={x1} | x2={x2} ')