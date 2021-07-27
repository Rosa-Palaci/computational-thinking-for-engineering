import random
import math
import statistics

'''Falta conteo de puntos'''

print("Calcula el promedio de estos numeros")
for veces in range (4):
    print("Los numeros son:")
    numeros1= random.randint(1,20)
    numeros2= random.randint(1,20)
    numeros3= random.randint(1,20)
    numeros4= random.randint(1,20)
    numeros5= random.randint(1,20)
    numeros6= random.randint(1,20)
    numeros7= random.randint(1,20)
    numeros8= random.randint(1,20)
    numeros9= random.randint(1,20)
    numeros10= random.randint(1,20)
    print (numeros1, numeros2, numeros3, numeros4, numeros5, numeros6, numeros7, numeros8, numeros9, numeros10)
    numeros= (numeros1, numeros2, numeros3, numeros4, numeros5, numeros6, numeros7, numeros8, numeros9, numeros10)
    respuesta_correcta=(numeros1+numeros2+numeros3+numeros4+numeros5+numeros6+numeros7+numeros8+numeros9+numeros10) / 10
    print(respuesta_correcta) #DEFINIR QUE LA RESPUESTA CORRECTA SOLO NECESITE 2 CIFRAS
    respuesta4= float(input(f"Tu respuesta es: "))
    if respuesta4 == respuesta_correcta:
        print("Respuesta correcta\n")
    else:
        print("Respuesta incorrecta\n")

print("Calcula la mediana de los numeros")
for veces in range (4):
    print("Los numeros son:")
    numeros_1= random.randint(1,20)
    numeros_2= random.randint(1,20)
    numeros_3= random.randint(1,20)
    numeros_4= random.randint(1,20)
    numeros_5= random.randint(1,20)
    numeros_6= random.randint(1,20)
    numeros_7= random.randint(1,20)
    numeros_8= random.randint(1,20)
    numeros_9= random.randint(1,20)
    numeros_10= random.randint(1,20)
    print (numeros_1, numeros_2, numeros_3, numeros_4, numeros_5, numeros_6, numeros_7, numeros_8, numeros_9, numeros_10)
    numeros_lista=(numeros_1, numeros_2, numeros_3, numeros_4, numeros_5, numeros_6, numeros_7, numeros_8, numeros_9, numeros_10)
    respuesta_correcta_2 = statistics.median(numeros_lista)
    print(respuesta_correcta_2) #DEFINIR QUE LA RESPUESTA CORRECTA SOLO NECESITE 2 CIFRAS
    respuesta4= float(input(f"Tu respuesta es: "))
    if respuesta4 == respuesta_correcta_2:
        print("Respuesta correcta\n")
    else:
        print("Respuesta incorrecta\n")
    print("Calcula la moda")
    
for veces in range (4):
    print("Los numeros son:")
    numeros_11= random.randint(1,20)
    numeros_12= random.randint(1,20)
    numeros_13= random.randint(1,20)
    numeros_14= random.randint(1,20)
    numeros_15= random.randint(1,20)
    numeros_16= random.randint(1,20)
    numeros_17= random.randint(1,20)
    numeros_18= random.randint(1,20)
    numeros_19= random.randint(1,20)
    numeros_20= random.randint(1,20)
    print (numeros_11, numeros_12, numeros_13, numeros_14, numeros_15, numeros_16, numeros_17, numeros_18, numeros_19, numeros_20)
    numeros_lista_2=(numeros_11, numeros_12, numeros_13, numeros_14, numeros_15, numeros_16, numeros_17, numeros_18, numeros_19, numeros_20)
    respuesta_correcta_3= statistics.mode(numeros_lista_2)
    print(respuesta_correcta_3) #DEFINIR QUE LA RESPUESTA CORRECTA SOLO NECESITE 2 CIFRAS
    respuesta4= float(input(f"Tu respuesta es: "))

if respuesta4 == respuesta_correcta_3:
    print("Respuesta correcta")
else:
    print("Respuesta incorrecta\n")