import random
import math
import random as rm
import math as mt
from random import choice
import time
from typing import final
import pyfiglet
import colorama
from colorama import Back, Fore, Style, init
import sys 


#MAGIC MATH GAME - titulo

colorama.init(autoreset=True)

if 1 == 1:
    print(f"\n{Fore.RED}M{Fore.LIGHTRED_EX}A{Fore.YELLOW}G{Fore.LIGHTYELLOW_EX}I{Fore.LIGHTGREEN_EX}C {Fore.GREEN}M{Fore.LIGHTCYAN_EX}A{Fore.CYAN}T{Fore.LIGHTBLUE_EX}H {Fore.BLUE}G{Fore.LIGHTMAGENTA_EX}A{Fore.MAGENTA}M{Fore.MAGENTA}E"'\n')
    if 2==1:
        p = 3

#Introduccion tiempo retraso
velocidad = float(input(f'{Fore.LIGHTYELLOW_EX}Ingresa la velocidad para las instrucciones: '))
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(float(f'{velocidad}'))

nombre = input(f'{Fore.YELLOW}Ingresa tu nombre: ')
delay_print(f'¡Bienvenid@ {nombre}!\n')
#Intro
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(float(f'{velocidad}'))

intro1 = str(f'\nA continuación tendrás que poner a prueba tus conocimientos y habilidades, contestando problemas matemáticos de cuatro áreas.')
intro2 = str(f'Los resultados se mostrarán una vez finalizado y respondido las cuatro áreas.')
delay_print(f'{intro1}\n{intro2}')

# Evalución 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(float(f'{velocidad}'))

evalua1 = str(f'\nCada ejercicio vale 2 puntos.')
evalua2 = str(f'Necesitas el 70% para aprobar el área.\n')
delay_print(f'{evalua1}\n{evalua2}')

# Codigo - Menu

menu = f"""
{Fore.LIGHTCYAN_EX}Bienvenido 💙
{Fore.YELLOW} 1 - Aritmética
{Fore.MAGENTA} 2 - Álgebra
{Fore.LIGHTGREEN_EX} 3 - Geometría
{Fore.BLUE} 4 - Probabilidad y estadística
{Fore.RED} 5 - Salir

{Fore.RED}Elige una area:  
"""
opcion = input(menu)

def area(area_elegida):
    if area_elegida == '1':
        print(f"{Fore.YELLOW}Empecemos con Aritmética")
        

    elif area_elegida == '2':
        print(f"{Fore.MAGENTA}Empecemos con Álgebra")
        

    elif area_elegida == '3':
        print(f"{Fore.MAGENTA}Empecemos con Geometría")
        

    elif area_elegida == '4':
        print(f"{Fore.BLUE}Empecemos con Probabilidad y estadística")
        

    elif area_elegida == '5':
        print(f"{Fore.LIGHTYELLOW_EX}Adios, regresa para seguir aprendiendo")

    else:
        print(f'{Fore.RED}Ingresa una opción correcta por favor, ¡Exito en tu prueba!😎')

area = area(opcion)