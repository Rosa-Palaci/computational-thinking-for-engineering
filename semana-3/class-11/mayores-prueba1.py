#
# 
def orden_asc(a, b, c):
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
    return menor, medio, mayor

for veces in range(2):
    a = int(input('Introduce el número 1: '))
    b = int(input('Introduce el número 2: '))
    c = int(input('Introduce el número 3: '))
    menor, medio, mayor = orden_asc(a, b, c)
    #print(f'Los números sin ordenar son: {a}, {b} y {c}\n')
    print(f'Los números en orden ascendente son: {menor}, {medio}, {mayor}')