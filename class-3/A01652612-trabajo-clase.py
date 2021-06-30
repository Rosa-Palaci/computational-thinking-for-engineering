#import math

#Primer ejemplo

#alfa = 30 #grados
#operacion = math.cos(alfa)

#print(operacion)

#Segundo ejemplo

#alfa = 30 #grados
#alfa_rad =alfa*math.pi/180

#operacion = math.cos(alfa_rad)

#print(operacion)

#Tercer ejemplo triangulo rectángulo
#Pide al usuario dos lados de un triángulo y el ángulo
#formado por ellos.
#Calcula el área y múestralo con el sig. mensaje:
#El área es ## unidades cuadradas.
import math

a = float(input('Ingresa el lado a: '))
b = float(input('Ingresa el lado b: '))
t = float(input('Ingresa el ángulo theta (en grados): '))

t_rad = t*math.pi/180
A = a*b*math.sin(t_rad)/2
print(f'El área es {A:.2f} unidades cuadradas')