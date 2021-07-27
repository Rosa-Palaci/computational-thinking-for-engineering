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
    
nombre = input(f'{Fore.RED}Ingresa tu nombre: ')
delay_print(f'{Fore.LIGHTRED_EX}¡Bienvenid@ {nombre}!\n')
#Intro
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    
intro1 = str(f'{Fore.YELLOW}\nA continuación tendrás que poner a prueba tus conocimientos y habilidades, contestando problemas matemáticos de cuatro áreas.')
intro2 = str(f'{Fore.LIGHTYELLOW_EX}Los resultados se mostrarán una vez finalizado y respondido las cuatro áreas.')
delay_print(f'{intro1}\n{intro2}')

# Evalución 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    
evalua1 = str(f'{Fore.LIGHTGREEN_EX}\nCada ejercicio vale 2 puntos.')
evalua2 = str(f'{Fore.GREEN}Necesitas el 70% para aprobar el área y seguir con la siguiente\n')
delay_print(f'{evalua1}\n{evalua2}')

# Codigo - Menu
def area(area_elegida):
    print(f"{Fore.CYAN}Empecemos con {area_elegida}" )

menu = f"""
{Fore.LIGHTCYAN_EX}Bienvenido 💙
1 - Aritmética
2 - Álgebra
3 - Geometría
4 - Probabilidad y estadística

Elige una area:  
"""
opcion = input(menu)

if opcion == '1':
    area("Aritmética")
elif opcion == '2':
    area("Álgebra")
elif opcion == '3':
    area("Geometría")
elif opcion == '4':
    area("Probabilidad y estadística")
else:
    print('Ingresa una opción correcta por favor')

#Algebra
#De un banco de preguntas Algebra, muestra al usuario una al azar
import random

question1 = 'La suma de cinco veces X y seis veces Y es:'
question2 = 'El perímetro P de un rectángulo es igual al doble de la suma de su songitud L y su anchura A'
question3 = 'B más el producto de O y U'
question4 = 'Resuelve para v'
question5 = 'Resuelve para x'
question6 = '(x**2+2x)*(x-5)'
question7 = 'La gráfica que corresponda a:' 
question8 = 'La gráfica que corresponda a:'
question9 = 'Calcula el punto del vértice de la función : f(x)= -2x**2 + 3x'
question10 = 'Divide{(6**5)+(x**4)+(4x**2)-(7x)+1} entre {(2x**2)+(x)-(3) el cociente es igual a:'
question11 = 'Dividir {10x**5-(4x**a)+(8x**3)+(6x**2)-(5x)+11 // (2x**2)-(2x)+4'
question12 = 'Racionalizar: foto {4raiz(x)-6} / {2raiz(3x)}'
question13 = 'Racionalizar el denominador y simplificar la expresión: foto {4raiz(2)} / {3raiz(xy**2)}'

#Preparando las preguntas con respuestas
question1 = 'La suma de cinco veces X y seis veces Y es:'
answer1 = '5x + 6y'
question2 = 'El perímetro P de un rectángulo es igual al doble de la suma de su songitud L y su anchura A'
answer2 = 'P=2(L+A)'
question3 = 'B más el producto de O y U'
answer3 = 'B+OU'
question4 = 'Resuelve para v'
answer4 = 'v=24+(3b*3)' 
question5 = 'Resuelve para x'
answer5 = 'x=18'
question6 = '(x**2+2x)*(x-5)'
answer6 = 'x**3-(3x**2)-(10x)'
question7 = 'La gráfica que corresponda a:' 
answer7 = '<---- -13 punto cerrado   punto abierto----->' 
question8 = 'La gráfica que corresponda a:'
answer8 = '<---- -4 punto cerrado  punto abierto 8 ------>'
question9 = 'Calcula el punto del vértice de la función : f(x)= -2x**2 + 3x'
answer9 = '(3/4,9/8)'
question10 = 'Divide{(6**5)+(x**4)+(4x**2)-(7x)+1} entre {(2x**2)+(x)-(3) el cociente es igual a:'
answer10 = '(3x**3)-(x**2)+5x-2'
question11 = 'Dividir {10x**5-(4x**a)+(8x**3)+(6x**2)-(5x)+11 // (2x**2)-(2x)+4'
answer11 = '30'
question12 = 'Racionalizar: foto {4raiz(x)-6} / {2raiz(3x)}'
answer12 = '{2x raiz (3) - 3raiz(3x)} / {3x} ' 
question13 = 'Racionalizar el denominador y simplificar la expresión: foto {4raiz(2)} / {3raiz(xy**2)}'
answer13 = '{18 raiz (8x**8 y**16)} / {xy**2} '

banco_questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13]

questions_azar = random.choice(banco_questions)

print(questions_azar)

def scoreAlgebre(question, correct_answer):
    print(question)
    ans = input('Respuesta: ')
    if ans == correct_answer:
        print('Correcto')
    else:
        print('Incorrecto')

questions_algebra = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13]
answers_algebra = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12, answer13]

opc = 0
while opc != answers_algebra:
    opc = menu()
    if opc == 2: #Algebra
        questionsAnswer = random.choice(questions_algebra)
        indice_questions = questions_algebra.index(questionsAnswer)
        scoreAlgebre((questionsAnswer, answers_algebra[indice_questions]))
    else:
        print('Nos vemos! 😉')
        break