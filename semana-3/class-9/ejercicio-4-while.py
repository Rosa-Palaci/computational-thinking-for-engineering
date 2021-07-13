#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 4

#Los articulos disponibles son los siguientes:
# A2 Pantalos $300
# B39 Gorra $150
# L10 Calcetines $90

compraFinal = 0

clave = ''

while clave != 'X':
    clave = input('\nTeclea la clave del artículo: ')
    if clave == 'A2':
        print('Costo de pantalones: $300')
        cantA2 = int(input('¿Cuántos articulos deseas adquirir?: '))
        compraFinal = compraFinal + 300*cantA2
    elif clave == 'B39':
        print('Costo de gorra: $150')
        cantB39 = int(input('¿Cuántos articulos deseas adquirir?: '))
        compraFinal = compraFinal + 150*cantB39
    elif clave == 'L10':
        print('Costo de caletines: $90')
        cantL10 = int(input('¿Cuántos articulos deseas adquirir?: '))
        compraFinal = compraFinal + 90*cantL10
    elif clave == 'X':
        print(f'\nCompra finalizada \nTotal a pagar es de ${compraFinal}')
    else:
        print('La clave es incorrecta, vuelve a intentarlo')