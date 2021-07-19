#De un banco de tres preguntas, muestra al usuario una al azar
import random

preg1 = '¿Cuánto es 1 + 1?'
preg2 = '¿Cuál es la capital de Francia?'
preg3 = '¿Cuál es la raíz cuadrada de 43455435?'

banco_preguntas = [preg1, preg2, preg3]

#Elige una pregunta al azar del banco de preguntas.
preg_azar = random.choice(banco_preguntas)

#Imprimir la pregunta al azar
print(preg_azar)

