#Pide al usuario 6 números y guárdalos 
# en una lista. Al final, imprimelos.
'''
def imprimeLista(lista):
    for elemento in lista:
        print(elemento, end = ' ')
    print()

listaNumeros = []
num = input('Teclea un número: ')
listaNumeros.append(num)
imprimeLista(listaNumeros)

num = float(input('Teclea un número: '))
listaNumeros.append(num)
imprimeLista(listaNumeros)'''

#De un banco de cuatro pregunto, muestra al usuario tres al azar (sin repetir)

import random

preg0 = '¿Cuánto es 1 + 1?'
preg1 = '¿Cuál es la capital de Francia?'
preg2 = '¿Cuál es la raíz cuadrada de 43455435?'
preg3 = '¿Cuánto es 5*3?'

banco_preguntas = [preg0, preg1, preg2, preg3]

for veces in range(3):
    #Elige una pregunta al azar del banco de preguntas.
    preg_azar = random.choice(banco_preguntas)

    # Imprimir la pregunta al azar
    print(preg_azar)

    #Eliminar la pregunta del banco de preguntas.
    banco_preguntas.remove(preg_azar)