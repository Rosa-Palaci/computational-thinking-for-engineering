#Proyecto integrador: Segunda entrega

#Realiza la codificación inicial de tu proyecto. Asegúrate de que usas los siguientes elementos:
# Operaciones aritméticas
# Condicionales
# Ciclos
# Funciones
# Listas

#imports
import pyfiglet

import colorama
from colorama import Back, Fore, Style, init

import sys 
import time

#MAGIC MATH GAME - titulo
colorama.init(autoreset=True)

if 1 == 1:
    print(f"\n{Fore.RED}M{Fore.LIGHTRED_EX}A{Fore.YELLOW}G{Fore.LIGHTYELLOW_EX}I{Fore.LIGHTGREEN_EX}C {Fore.GREEN}M{Fore.LIGHTCYAN_EX}A{Fore.CYAN}T{Fore.LIGHTBLUE_EX}H {Fore.BLUE}G{Fore.LIGHTMAGENTA_EX}A{Fore.MAGENTA}M{Fore.MAGENTA}E"'\n')
    if 2==1:
        p = 3
        
#Introduccion tiempo retraso
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    
nombre = input('Ingresa tu nombre: ')
delay_print(f'¡Bienvenid@ {nombre}!\n')
#Intro
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    
intro1 = str('\nA continuación tendrás que poner a prueba tus conocimiento y habilidades, contestando problemas matemáticos de cuatro áreas.')
intro2 = str('Los resultados se mostrarán una vez finalizado y respondido las cuatro áreas.')
delay_print(f'{intro1}\n{intro2}')

# Evalución 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    
evalua1 = str(f'\nCada ejercicio vale 2 puntos')
evalua2 = str(f'Necesitas el 70% para aprobar el área y seguir con la siguiente\n')
delay_print(f'{evalua1}\n{evalua2}')
# Codigo
# def calificador ():
    # if ejercicioCorrecto == 25:
    #     pass
    # if resultado menor= 50:
    #     print(f'{resultado} se requerirán 25 ejercicios para poder pasar el nivel')
    # if resultado mayor = 50 and menor que 70:
    #     print('se requerirán 20 ejercicios')
    # if mayor= 70:
    #     print('se requerirán 15 ejercicios')

#De un banco de preguntas algebraicas
import random

question1 = '¿Cuánto es 1 + 1?'
question2 = '¿Cuál es la capital de Francia?'
question3 = '¿Cuál es la raíz cuadrada de 43455435?'

banco_preguntas = [preg1, preg2, preg3]

#Elige una pregunta al azar del banco de preguntas.
preg_azar = random.choice(banco_preguntas)

#Imprimir la pregunta al azar
print(preg_azar)
