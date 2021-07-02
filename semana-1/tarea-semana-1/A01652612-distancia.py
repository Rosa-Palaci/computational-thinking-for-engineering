#Actividad - Programas que usan estatutos de decisión con operaciones aritméticas
#Distancia
#Rosa Vanessa Palacios Beltran
#A01652612

#Realiza las siguientes operaciones en un programa 
#la distancia entre dos puntos del plano cartesiano.

import math

#Puntos
#pi (x1, y1)
#pf (x2, y2)

print('Los puntos deben ir en términos (x,y)')

#x1 = float(input("punto inicial de x: "))
#y1 = float(input("punto inicial de y: "))

p1 = input('Punto 1: ')
x1 = float(p1[1])
y1 = float(p1[3])
x2 = float(input("punto final de x: "))
y2 = float(input("punto final de y: "))

print(f'Punto inicial:( {x1}, {y1} )')
print(f'Punto final:( {x2}, {y2} )')

dist = math.sqrt( ( (x2 - x1)**2 ) + ( (y2-y1)**2 ) )

print(f'La distancia entre los puntos es de: {dist:.2f}')