#Actividad en clase - Estatutos de decisión - 1
#Rosa Vanessa Palacios Beltran
#A01652612

lado_x = int(input('Ingrese valor para lado x: '))
lado_y = int(input('Ingrese valor para lado y: '))
lado_z = int(input('Ingrese valor para lado z: '))

if (lado_x, lado_y, lado_z) == 0:
    print('Valores no validos')
    quit()
else:
    if (lado_x + lado_y) > lado_z:
        print
    else:
        print('Valores no validos')
        quit()
    if (lado_x + lado_z) > lado_y:
        print
    else:
        print('Valores no validos')
        quit()
    if (lado_y + lado_z) > lado_x:
        print
    else:
        print('Valores no validos')
        quit()

print(f'Los valores de (x, y, z) son: {lado_x, lado_y, lado_z}')

if lado_x == lado_y == lado_z:
    tipo = 'equilatero'#el triángulo equilátero tiene 3 lados iguales
elif lado_x == lado_y:
    tipo = 'isósceles'#el isósceles tiene 2 lados iguales 
elif lado_x == lado_z:
    tipo = 'isósceles'
elif lado_y == lado_z:
    tipo = 'isósceles'
elif lado_x != lado_y != lado_z:
    tipo = 'escaleno'#el escaleno tiene los 3 lados diferentes
else:
    print('No existe')
    quit()

print(f'El tipo de triángulo es {tipo}')