#Ejercicio en clase 4 - 01/07/21
#Rosa Vanessa Palacios Beltran
#A01652612

#Pide al usuario su nombre y su edad
#Muestra el siguiente mensaje:
#Hola -nombre-, según tu edad eres mayor de edad
#Al finalizar, despidete del usuario.

#Imprime si true es mayor edad, y true y false see you later
#nombre = input('Teclea tu nombre: ')
# edad = int(input('Teclea tu edad: '))

#if edad >= 18:
#    print(f'Hola {nombre}, eres mayor de edad')

#print('See you later')

#Caso solo imprime si es verdadero
#if edad >= 18:
#    print(f'Hola {nombre}, eres mayor de edad')
#    print('See you later')

# Caso True un camino y False camino diferente que al final se unen

nombre = input('Teclea tu nombre: ')
edad = int(input('Teclea tu edad: '))

if edad >= 18:
    print(f'Hola {nombre}, eres mayor de edad')
else:
    print(f'Hola {nombre}, eres menor de edad')

print('See you later!')