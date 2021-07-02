#Actividad - Programas que usan estatutos de decisión con operaciones aritméticas
#Calculos
#Rosa Vanessa Palacios Beltran
#A01652612

#Realiza las siguientes operaciones en un programa de Python

import math

a = 4
b = 5

print(f'Valor de a: {a}')
print(f'Valor de b: {b}')


oper3 = ((a**3)+(2*(b**2))) / ((2*((a+b)**2)) + (4*((a-b)**2)))

oper4 = ((2*((a+b)**2)) + (4*((a-b)**2))) / ((a*b)**2)

oper5 = ((math.sqrt((a+b)**2) + (2**(a+b))) / ( ( (2*a) + (2*b) )**2 ) )

print(f'El resultado de oper3 es: {oper3}')
print(f'El resultado de oper4 es: {oper4}')
print(f'El resultado de oper5 es: {oper5}')