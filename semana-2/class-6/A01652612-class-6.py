#Ejercicios clase-6
#Rosa Vanessa Palacios Beltran
#A01652612

#Tarea de clase 5

import random

'''
a = int(input('Número a: '))
b = int(input('Número b: '))
c = int(input('Número c: '))
'''

'''
a = random.radint(0,20)
b = random.radint(0,20)
c = random.radint(0,20)
'''

a = 10
b = 2
c = 5

print(f'Los númros sin ordenar son: {a}, {b} y {c}\n')


if a > b:
    if a > c:
        mayor = a
    if b > c:  
        medio = b  
        menor = c
    else: 
        medio = c
        menor = b
    else: # significa que c > b
        medio = c
        menor = b
elif b > a and b > c:
    mayor = b
    if a > c:
        medio = a
        menor = c
    else: 
        medio = c
        menor = a
else: #Significa que 'c' es el mayor
    mayor = c
    if a > b:
        medio = a
        menor = b
    else: 
        medio = b
        menor = a

print(f'Los números en orden ascendente son: {menor}, {medio}, {mayor}')