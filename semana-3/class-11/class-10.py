#Actividad Evaluable - Programas que utilizan funciones
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 1
#Libreria numpy
import math

def dividir(num, den):
    if den == 0: #La división no está definida
        return math.nan
    else:
        return num/den

num1 = float(input('Teclea el numerador: '))
den1 = float(input('Teclea el denominador: '))
div1 = dividir(num1, den1)
print(f'{num1}/{den1} = {div1}\n')