#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 5

'''
Muestra una serie de número que empiezan en a y se vayan 
incrementando de 5 en 5 hasta llegar a b, donde a y b son 
dos número capturados por el usuario y asume que a siempre 
es menor que b 

Nota que a y b no necesariamente son múltiplos de 5, y que 
debe mostrar todos los números que sean menor o igual a b.
'''
a = int(input('Introduce \'a\': '))
b = int(input('Introduce \'b\': '))

for num in range(a, b + 1, 5):
    print(num, emd = ' ')