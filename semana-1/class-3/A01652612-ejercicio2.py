#Ejercicio 2
#Rosa Vanessa Palacios Beltran
#A01652612

#El área y volumen de una esfera se calcula con las siguientes fórmulas:

#Escribe un programa que pida el valor del radio y muestre su área y su volumen.

import math

radio = float(input("Ingrese el radio de la esfera: "))

def area_esfera(radio):
    area = 4 * math.pi * radio ** 2

    return area

def volumen(radio):
    resultado = (4/3) * math.pi * radio **3

    return resultado

radio = 5
print("El área de la esfera es de: ", area_esfera(radio))
print("El volumen de la esfera es de: ",volumen(5))