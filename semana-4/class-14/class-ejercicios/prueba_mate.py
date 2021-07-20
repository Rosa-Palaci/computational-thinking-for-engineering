import random

def menu():
    print('\n¿Qué área deseas practicar?')
    print('1) Aritmética\n2) Álgebra\n3) Salir')
    opc = int(input('Teclea tu opción: '))
    while opc < 1 or opc > 3: #Opción inválida
        opc = int(input('Opción inválida, vuelve a intentarlo: '))
        
    return opc

def genera_califica_pregunta(pregunta, respuesta_correcta):
    print(pregunta)
    resp = input('Respuesta: ')
    if resp == respuesta_correcta:
        print('Correcto')
    else:
        print('Incorrecto')
    
       

#Preparando las preguntas con respuestas
preg0Ar = '¿Cuánto es 1 + 1? \na)2  b)3  c)4' 
resp0Ar = 'a'
preg1Ar = 'Teclea el resultado de 2*3 + 1'
resp1Ar = '7'
preg2Ar = '¿Cuánto es 3^2? \na)6  b)9  c)12  d) 24'
resp2Ar = 'b'

preguntas_aritmetica = [preg0Ar, preg1Ar, preg2Ar]
respuestas_aritmetica = [resp0Ar, resp1Ar, resp2Ar]

preg0Al = 'Simplifica 3x + x \na)3x^2  b)2x  c)4x' 
resp0Al = 'c'
preg1Al = 'Resuelve 6x = 12'
resp1Al = '2'
preg2Al = 'Solución positiva de x^2 - 4 = 0\na)0  b)1  c)2'
resp2Al = 'c'

preguntas_algebra = [preg0Al, preg1Al, preg2Al]
respuestas_algebra = [resp0Al, resp1Al, resp2Al]
#====================================================

opc = 0
while opc != 3:
    opc = menu()
    if opc == 1: #Aritmética
        pregAr = random.choice(preguntas_aritmetica)
        indice_preg = preguntas_aritmetica.index(pregAr)
        genera_califica_pregunta(pregAr, respuestas_aritmetica[indice_preg])
    elif opc == 2: #Álgebra
        pregAl = random.choice(preguntas_algebra)
        indice_preg = preguntas_algebra.index(pregAl)
        genera_califica_pregunta(pregAl, respuestas_algebra[indice_preg])
    else:
        print('Hasta luego')
        break
    
        
    


