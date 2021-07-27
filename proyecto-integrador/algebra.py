from random import choice
import time
from typing import final

import pyfiglet

import colorama
from colorama import Back, Fore, Style, init

import sys

def area(area_elegida):
    if area_elegida == '2':
        print(f"{Fore.CYAN}Empecemos con Álgebra")

        def correct(a,b,c,d):
            a +=1
            d += 1
            borrar = b.index(c)
            del b[borrar] # para no generar la pregunta
            print("Correcto🥳")
            return a,b,d

        def incorrect(a,b,c):
            a += 1
            borrar= b.index(c)
            del b[borrar]
            print("Incorrecto😭")
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

        scoreAlgebra = 0
        print('Te pedimos que contestes con una letra cada respuesta, de lo contrario tu respuesta no será valida')

        inicio = time.time() #toma la hora
        quest_random = ((list(questions.keys())))
        numeracion = 1

        while quest_random != []:
            print(f"\nPregunta#,{numeracion}")
            num = choice(quest_random)
            print(questions[num])

            if num == 1:
                a = print("a)5y + 6x")
                b = print("b)x+x+x+x+x+y+y+y+y+y+y")
                c = print("c)5x + 6y")# respuesta correcta
                d = print("d)5(X)-6(y)")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'c':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 2:
                a = print("a)P=2L+A")
                b = print("b)P=L+2A")
                c = print("c)P=4L+4A")
                d = print("d)P=2(L+A)")# respuesta correcta
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'd':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)
            
            if num == 3:
                a = print("a)B+1(OOU)")
                b = print("b)B-(O+U)")
                c = print("c)B+OU")# respuesta correcta
                d = print("d)B + (O)+(U)")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'c':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 4:
                a = print("a) v=24+(3b*3)")# respuesta correcta
                b = print("b) v=72b")
                c = print("c) v=216b")
                d = print("d) v=72+(3b)")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'a':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)
                    
            if num == 5:
                a = print("a) x=72")
                b = print("b) x=18")# respuesta correcta
                c = print("c) x=1.88")
                d = print("d) x=12(4/6)")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'b':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 6:
                a = print("a) ")
                b = print("b) x**3-(3x**2)-(10x)")# respuesta correcta
                c = print("c) ")
                d = print("d) ")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'b':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 7:
                a = print("a) ")
                b = print("b) <---- -13 punto cerrado   punto abierto----->")# respuesta correcta
                c = print("c) ")
                d = print("d) ")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'b':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 8:
                a = print("a) ")
                b = print("b) ")
                c = print("c) <---- -4 punto cerrado  punto abierto 8 ------>")# respuesta correcta
                d = print("d) ")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'c':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 9:
                a = print("a) ")
                b = print("b) ")
                c = print("c) ")
                d = print("d) (3/4,9/8)")# respuesta correcta
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'd':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 10:
                a = print("a) (3x**3)-(x**2)+5x-2")# respuesta correcta
                b = print("b) ")
                c = print("c) ")
                d = print("d) ")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'a':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 11:
                a = print("a) 30")# respuesta correcta
                b = print("b) 33")
                c = print("c) 23")
                d = print("d) 39")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'a':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 12:
                a = print("a) ")
                b = print("b) 30")
                c = print("c) {2x raiz (3) - 3raiz(3x)} / {3x} ")# respuesta correcta
                d = print("d) ")
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'c':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

            if num == 13:
                a = print("a) ")
                b = print("b) ")
                c = print("c) ")
                d = print("d) {18 raiz (8x**8 y**16)} / {xy**2} ")# respuesta correcta
                time1= time.time()
                Answer = input("Selecciona la respuesta correcta: ")
                time2= time.time()
                if Answer.upper() == 'd':
                    print("tiempo de repuesta: ", round(time2-time1,2))
                    scoreAlgebra,quest_random,numeracion = correct(scoreAlgebra,quest_random,num,numeracion)
                else:
                    numeracion,quest_random = incorrect(numeracion,quest_random,num)

        from pisa import nombre
        print(f"Nombre:{nombre}")
        print(f"Tu puntaje es: {scoreAlgebra}")
        finalAlgebra = time.time()
        minutes = (int(finalAlgebra-inicio)//60)
        seconds = (int(finalAlgebra-inicio)%60)
        if minutes == 1:
            print(f"Su tiempo para Álgebra fue de: {minutes}:{seconds}")
        else:
            print(f"Su tiempo fue de: {minutes}:{seconds}")
        if scoreAlgebra == 26: # 100
            print("Puntaje Prefecto🥳")
        elif scoreAlgebra >= 20.8 and scoreAlgebra <= 23.4: #80 - 90
            print("Muy bien, sigue practicando✨")
        elif scoreAlgebra >= 18.2 and scoreAlgebra <= 20.54: #70 - 79
            print("Bien, tu puedes🦾")
        elif scoreAlgebra >= 15.6 and scoreAlgebra <= 17.94: #60 - 69
            print("Casi lo logras🤗")
        elif scoreAlgebra >= 15.6 and scoreAlgebra <= 17.94: #60 - 69
            print("No te rindas, estudia un poco más🤓👻")