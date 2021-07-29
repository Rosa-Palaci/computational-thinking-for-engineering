import random
import math
import statistics

print ("\n")
print ("A continuación se desplegará el cuestionario de Geometría: ")
print ("\n")
print ("Calcula mediante la formula de Herón el area del triangulo")
print ("\n")
for veces in range (6):
    while True:
        a1= random.randint(1,20)
        b1= random.randint(1,20)
        c1= random.randint(1,20)
        if a1+b1>c1 and b1+c1>a1 and a1+c1>b1:
            break
    print(f"El lado a mide {a1}")
    print(f"El lado b mide {b1}")
    print(f"El lado c mide {c1}")
    s= (a1+b1+c1)/2
    A= s * (s-a1) * (s-b1) * (s-c1)
    rA=math.sqrt(A)
    print ("\n")
    print("Cual es el area?")
    respuesta1= float(input(f"Tu respuesta es (escribela con 2 decimales): "))
    if respuesta1 == round(rA,2):
        puntos += 1
        print ("¡Correcto!")
        print ("Puntaje actual: ", puntos)
        print ("\n")
    else:
        print("Respuesta errónea")
        print ("Puntaje actual: ", puntos)
        print ("\n")
    print("--------------------------------------------------------------------------------------------------------")
    print("Siguiente bloque\n")
    print("Calcula la hipotenusa usando el Teorema de pitágoras")
    print ("\n")
    for veces in range (6):
        a= random.randint(10,50)
        b= random.randint(10,50)
        print(f"El lado a mide {a}")
        print(f"El lado a mide {b}")
        hipotenusa=math.sqrt(a ** 2 + b ** 2)
        print ("\n")
        print("Cual es la hipotenusa?")
        respuesta= float(input(f"Tu respuesta es (escribela con 2 decimales): "))
        if respuesta == round(hipotenusa,2):
            puntos += 1
            print ("¡Correcto!")
            print ("Puntaje actual: ", puntos)
            print ("\n")
        else:
            print("Respuesta errónea")
            print ("Puntaje actual: ", puntos)
            print ("\n")