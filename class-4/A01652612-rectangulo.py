#Ejercicio 5 en clase 4 - 01/07/21
#Rosa Vanessa Palacios Beltran
#A01652612

#Realiza un programa que determine si un cuadrilatero es un rectángulo o no.

a = 10
b = 20
c = 20
d = 100

if (a == b) and (b == c) and (c == d):
    print('Es un cuadrado')

elif a == d and c == b:
    print('Rectángulo')
else:
    print('No es un rectángulo')