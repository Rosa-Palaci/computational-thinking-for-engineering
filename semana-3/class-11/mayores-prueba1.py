import random
a = random.randint(0, 200)
b = random.randint(0, 200)
c = random.randint(0, 200)

print(f'Los números sin ordenar son: {a}, {b} y {c}\n')

if a > b and a > c:
    mayor = a
    if b > c:
        medio = b
        menor = c
    else: #Significa que c > b
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