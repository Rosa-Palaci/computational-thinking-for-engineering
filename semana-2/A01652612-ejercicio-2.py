#Actividad en clase - Estatus de decisión -2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejericicio # 2

# La fórmula para sacar la distancia entre dos puntos es:
# ditancia = raiz cuadrada ((x2 - x1)**2 + (y2- y1)**2)

import math

radio = float(input('Ingresar el radio del círculo: '))
puntoCentro = float(input('Ingresar coordenadas del centro del círculo: '))
punto = float(input('Ingresar coordenadas de un punto distinto al centro del círculo: '))

if puntoCentro <= 0:
    print('Coordenada no valida, intente otra forma.')
    quit()
elif puntoCentro == 1:
    print(f'El {puntoCentro} se encuentra dentro del círculo')
else:
    print(f'El {puntoCentro} se enccuentra fuera del círculo')

circunferancia = input('dentro,fuera o sobre la circunfernacia')

distancia = math.sqrt( ( (x2 - x1)**2 ) + ( (y2-y1)**2 ) )

print(f'La distancia entre los puntos es de: {distancia:.2f} por lo tanto el punto esta {circunferancia}')