#Clase-8
#Rosa Vanessa Palacios Beltran
#A01652612

#tip tiempo retraso
'''
import sys 
import time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    
var  = 10
delay_print(f'La variable es {var}')
'''
#Formula una pregunta de opcion múltiple al usuario.
#Mientras la respuesta sea incorrecta, sigue haciendo la misma pregunta.

print('¿Quién escribió el libro de Azteca?')
print('a)Crevantes \tb)Stepshen King \tc)Gary Jennings \td)Octavio Paz')
resp = input('Teclea tu respuesta: ')

intentos = 1
while intentos < 3:
    if resp != 'c':
        resp = input('Repsuesta incorrecta, vuelve a intentarlo: ')
        intentos = intentos + 1
    
    if intentos == 3:
        print('Te quedaste sin intentos')

    if resp == 'c':
        print('Respuesta correcta')
        break