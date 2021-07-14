#Actividad en clase - Funciones
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 1
#¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:
'''
def uno (a, b) :
     a = a + 5
     b += 10
     print(a)
     print(b)
     return b

x = 5
y = 8
z = uno(x, y)
print(x)
print(y)
print(z)

#Ejercicio 2
#¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:
def func1 (a, b):
      print(f'{a} {b}')

def func2 (x, y):
      x = 10
      y *= 2
      func1 (y, x)

p = 2
q = 3
func2(p,q)
func1(p,q)

#Ejercicio 3
#¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:
def uno (a, b) :
    a = a // 3
    return a + b

def main():
    x = 10
    y = 40
    z = uno(y, x)
    print(z)

main()


#Ejercicio 4
#¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:
def uno (a, b):
    print(a, b)

def dos(x, y):
    x = 3
    y = 6
    uno(x, y)

def main() :
    p = 5
    q = 7
    dos(p,q)

main()


#Ejercicio 5
#¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:
def tres(x, y):
    x = 3
    y = 6

def main() :
    p = 10
    q = 20
    tres(p,q)
    print(p, q)

main()

'''

#Ejercicio 6
#¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:
def calculo(x, y):
    z = x + y
    return z

def main():
    p = 5
    q = 2
    r = 10
    r = calculo(p,q)
    print(r)

main()