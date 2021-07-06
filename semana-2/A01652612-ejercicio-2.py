#Actividad en clase - Estatus de decisión -2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejericicio # 2

import math

print('Acontinuación ingresa el punto centro del círculo')

x1 = float(input("punto centro de x: "))
y1 = float(input("punto centro de y: "))
puntoCentro = str(input(f'Coordenadas del centro del círculo: ({x1},{y1})'))

radio = float(input('Ingresar el radio del círculo: '))

if radio < x1:
    print('Error')
    quit()
elif radio < y1:
    print('Error')
    quit()
else:
    print('Elige un punto diferente o igual al centro del círculo')

x2 = float(input("punto de x: "))
y2 = float(input("punto de y: "))
punto = str(input(f'Coordenadas del punto elegido son:({x2},{y2})'))

distancia = math.sqrt( ( (x2 - x1)**2 ) + ( (y2-y1)**2 ) )

print(f'La distancia entre los puntos es de: {distancia:.2f}')

if ({x2},{y2}) >= ({x1},{y1}):
    circunferancia = print(f'El punto en ({x2},{y2}) se encuentra fuera del círculo')
    ubicacion = 'fuera de la circunferencia' 
elif ({x2},{y2}) <= ({x1},{y1}):
    circunferancia = print(f'El punto en ({x2},{y2}) se encuentra dentro del círculo')
    ubicacion = 'dentro de la circunferencia' 
elif ({x2},{y2}) == ({x1},{y1}):
    circunferancia = print(f'El punto en ({x2},{y2}) se encuentra sobre la circunferencia')
    ubicacion = 'sobre de la circunferencia' 

print(f'Por lo tanto el punto elegido esta {ubicacion}')