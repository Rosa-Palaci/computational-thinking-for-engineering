#Ejercicio 2 en clase 4 - 01/07/21
#Rosa Vanessa Palacios Beltran
#A01652612

#Pide al usuario su edad, y muestra el mensaje correspondiente
#dependiendo de su edad
#Mayor a 60 años: Te toca vacunarte el 20 de julio
#Entre 40 y 59 años: Vacúnate el 28 de julio
#Entre 18 y 39 años: Vacúnate el 5 de agosto
#Menor a 18: Vacúnate el 10 de agosto
#Nota: si el usuario ingresó una edad incorrecta, notificaselo.

usuario = str(input('Teclea tu nombre: '))
edad = int(input('Teclea tu edad: '))

if 60 <= edad <= 130:
    print('Te toca vacunarte el 20 de julio')
    print('Dirígase a la casilla 1')
elif 40 <= edad <= 59:
    print('Te toca vacunarte el 28 de julio')
    print('Dirígase a la casilla 2')
elif 18 <= edad <= 39:
    print('Te toca vacunarte el 5 de agosto')
    print('Dirígase a la casilla 3')
elif 12 <= edad <= 17:
    print('Te toca vacunarte el 10 de agosto')
    print('Dirígase a la casilla 4')
else:
    print('Tu edad no cumple los requisitos')

print(f'Hasta pronto {usuario}')