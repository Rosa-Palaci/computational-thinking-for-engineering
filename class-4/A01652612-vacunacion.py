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
    fecha = '20 de julio'
    num_casilla = '1'
elif 40 <= edad <= 59:
    fecha = '28 de julio'
    num_casilla = '2'
elif 18 <= edad <= 39:
    fecha = '5 de agosto'
    num_casilla = '3'
elif 12 <= edad <= 17:
    fecha = '10 de agosto'
    num_casilla = '4'
else:
    print('Tu edad no cumple los requisitos')
    quit() #Termina el programa de forma abrupta

print(f'Te toca vacunarte el {fecha}')
print(f'Dirígase a la casilla {num_casilla}')
print(f'Hasta pronto {usuario}')