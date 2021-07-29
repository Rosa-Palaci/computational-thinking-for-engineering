from abc import abstractstaticmethod
from random import choice
import time
from typing import final
import pyfiglet
import colorama
from colorama import Back, Fore, Style, init
import sys

score_algebra = 0 #varible para punto de algebra
correct_algebra = 0 #variable para conteo de las correctas
wrong_algebra = 0 #variable para conteo de las correctas
correct_ans_algebra = [] # se guardaran 
wrong_ans_algebra = []
wrong = 0


questions ={1:"La suma de cinco veces X y seis veces Y es:",
            2:"El perímetro P de un rectángulo es igual al doble de la suma de su songitud L y su anchura A",
            3:"B más el producto de O y U",
            4:"Resuelve para v",
            5:"Resuelve para x",
            6:"(x**2+2x)*(x-5)",
            7:"La gráfica que corresponda a:",
            8:"La gráfica que corresponda a:",
            9:"Calcula el punto del vértice de la función : f(x)= -2x**2 + 3x",
            10:"Divide{(6**5)+(x**4)+(4x**2)-(7x)+1} entre {(2x**2)+(x)-(3) el cociente es igual a:",
            11:"Dividir {10x**5-(4x**a)+(8x**3)+(6x**2)-(5x)+11 // (2x**2)-(2x)+4",
            12:"Racionalizar: foto {4raiz(x)-6} / {2raiz(3x)}",
            13:"Racionalizar el denominador y simplificar la expresión: foto {4raiz(2)} / {3raiz(xy**2)}"}


print(f'{Fore.LIGHTMAGENTA_EX}Te pedimos que contestes con una letra cada respuesta, de lo contrario tu respuesta no será valida')
    
def correct(a,b,c,d):
    '''(scoreAlgebra,quest_random,num,numeracion)'''
    a += 2
    d += 1
    borrar = b.index(c)
    del b[borrar] # para no generar la pregunta
    print(f"{Fore.GREEN}Correcto🥳")
    return a,b,d
    '''(scoreAlgebraMal,numeracion,quest_random,num)'''
def incorrect(a,b,c):
    a += 1
    borrar= b.index(c)
    del b[borrar]
    print(f"{Fore.RED}Incorrecto😭")
    return a,b

questions ={1:"La suma de cinco veces X y seis veces Y es:",
                    2:"El perímetro P de un rectángulo es igual al doble de la suma de su songitud L y su anchura A",
                    3:"B más el producto de O y U",
                    4:"Resuelve para v",
                    5:"Resuelve para x",
                    6:"(x**2+2x)*(x-5)",
                    7:"La gráfica que corresponda a:",
                    8:"La gráfica que corresponda a:",
                    9:"Calcula el punto del vértice de la función : f(x)= -2x**2 + 3x",
                    10:"Divide{(6**5)+(x**4)+(4x**2)-(7x)+1} entre {(2x**2)+(x)-(3) el cociente es igual a:",
                    11:"Dividir {10x**5-(4x**a)+(8x**3)+(6x**2)-(5x)+11 // (2x**2)-(2x)+4",
                    12:"Racionalizar: foto {4raiz(x)-6} / {2raiz(3x)}",
                    13:"Racionalizar el denominador y simplificar la expresión: foto {4raiz(2)} / {3raiz(xy**2)}"}

from pisa import nombre
inicio = time.time() #toma la hora
username = print(f'Comencemos {nombre}')
quest_random = ((list(questions.keys())))
numeracion = 1

while quest_random != []:
    print(f"\nPregunta # {numeracion}")
    num = choice(quest_random)
    print(questions[num])
    if num == 1:
        A = print("A)5y + 6x")
        B = print("B)x+x+x+x+x+y+y+y+y+y+y")
        C = print("C)5x + 6y")# respuesta correcta
        D = print("D)5(X)-6(y)")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        if Answer.upper() == 'C':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 2:
        A = print("A)P=2L+A")
        B = print("B)P=L+2A")
        C = print("C)P=4L+4A")
        D = print("D)P=2(L+A)")# respuesta correcta
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'D':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 3:
        A = print("A)B+1(OOU)")
        B = print("B)B-(O+U)")
        C = print("C)B+OU")# respuesta correcta
        D = print("D)B + (O)+(U)")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'C':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 4:
        A = print("A) v=24+(3b*3)")# respuesta correcta
        B = print("B) v=72b")
        C = print("C) v=216b")
        D = print("D) v=72+(3b)")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'A':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 5:
        A = print("A) x=72")
        B = print("B) x=18")# respuesta correcta
        C = print("C) x=1.88")
        D = print("D) x=12(4/6)")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'B':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 6:
        A = print("A) ")
        B = print("B) x**3-(3x**2)-(10x)")# respuesta correcta
        C = print("C) ")
        D = print("D) ")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'B':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 7:
        A = print("A) ")
        B = print("B) <---- -13 punto cerrado   punto abierto----->")# respuesta correcta
        C = print("C) ")
        D = print("D) ")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'B':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 8:
        A = print("A) ")
        B = print("B) ")
        C = print("C) <---- -4 punto cerrado  punto abierto 8 ------>")# respuesta correcta
        D = print("D) ")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'C':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 9:
        A = print("A) ")
        B = print("B) ")
        C = print("C) ")
        D = print("D) (3/4,9/8)")# respuesta correcta
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'D':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 10:
        A = print("A) (3x**3)-(x**2)+5x-2")# respuesta correcta
        B = print("B) ")
        C = print("C) ")
        D = print("D) ")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'A':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 11:
        A = print("A) 30")# respuesta correcta
        B = print("B) 33")
        C = print("C) 23")
        D = print("D) 39")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'A':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 12:
        A = print("A) ")
        B = print("B) 30")
        C = print("C) {2x raiz (3) - 3raiz(3x)} / {3x} ")# respuesta correcta
        D = print("D) ")
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'C':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)

    if num == 13:
        A = print("A) ")
        B = print("B) ")
        C = print("C) ")
        D = print("D) {18 raiz (8x**8 y**16)} / {xy**2} ")# respuesta correcta
        time1= time.time()
        Answer = input(f"{Fore.LIGHTYELLOW_EX}Selecciona la respuesta correcta: ")
        time2= time.time()
        print("tiempo de repuesta: ", round(time2-time1,2))
        if Answer.upper() == 'D':
            print("Tiempo de repuesta: ", round(time2-time1,2))
            score_algebra,quest_random,numeracion = correct(score_algebra,quest_random,num,numeracion)
        else:
            numeracion,quest_random = incorrect(numeracion,quest_random,num)


print(f"\nTu puntaje es: {score_algebra*2}")
final_algebra = time.time()
minutes = (int(final_algebra-inicio)//60)
seconds = (int(final_algebra-inicio)%60)
if minutes == 1:
    pass
else:
    print(f"Su tiempo para Álgebra fue de: {minutes}:{seconds}\n")

if score_algebra == 13: # 100
    print("Puntaje Prefecto🥳\n")
elif score_algebra >= 10.4 and score_algebra <= 11.7:
    print("Muy bien, sigue practicando✨\n")
elif score_algebra >= 7.8 and score_algebra <= 9.1:
    print("Bien, tu puedes mejorar🦾\n")
elif score_algebra >= 0 and score_algebra <= 6.5:
    print("No te rindas, estudia un poco más🤓👻\n")