#Actividad en clase - Estatus de decisión -2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio # 1

a = int(input('Ingresa tu primer número: '))
b = int(input('Ingresa tu segundo número: '))
c = int(input('Ingresa tu tercer número: '))


if((a <= b) and (a <= c)):

    menor = a

    if(b <= c):
        medio = b
        mayor = c
    else:
        medio = c
        mayor = b

elif((b <= a) and (b < c)):

    menor = b

    if(a <= c):
        medio = a
        mayor = c
    else:
        medio = c
        mayor = a
else:
    menor = c

    if(a <= b):
        medio = a
        mayor = b
    else:
        medio = b
        mayor = a

print(f'Ordenados de menor a mayor: {str(menor)}, {str(medio)}, {str(mayor)}')