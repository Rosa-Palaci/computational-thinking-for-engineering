# problema 1 
x = 35
if x % 3 == 0:
    print('M1')
else:
    print('M2')
#Respuesta 1:
'''
x = 35
el residuo de 35/3 es igual a
 0 imprime M1 sino (else: imprime M2)'''

# problema 2
for var in range(0, 11, 3):
    print(var, end = ', ')
#Respuesta 2:
'''
rango de (0,11] 
que vaya de 3 en 3 empezando con 0 
y que al final de cada bucle ponga una , (como y espacio)
(0, 3, 6, 9,)
*0, 3, 6, 9,*'''


# problema 3
def f1(x):
    if x == 1:
        y = 1
        
    elif x == 6:
        y = 4
    else:
        y = 2
    print(f'{x} {y}')
    
        
def main(a):
    f1(a)
    
b = 3
main(b)
#Respuesta 2:
'''
empieza de main que b = 3
a = 3
main llama f1
a = x
entonces x = 3
- (si x == 1
y = 1 no se cumple)
- (si x == 6
y = 4 no se cumple)
si no y = 2 imprime x y 
x=3 
y=2
3 2

*3 2*'''