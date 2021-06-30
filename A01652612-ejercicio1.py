#Ejercicio 1
#Rosa Vanessa Palacios Beltran
#A01652612

#Escribe un programa que pida al usuario los valores a, b y c, y 
#calcule y muestre el área del triángulo usando esta fórmula.

import math

#Lados de un triángulo a,b y c
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** (1/2)

print("El área del triángulo es de: ", area)