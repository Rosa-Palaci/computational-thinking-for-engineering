#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 6

#Calcula el factorial de un numero n...

N = int(input('Teclea el número al que quieres calcularle el factorial: '))
mult = 1
for num in range(1, N + 1):
    mult = mult*num

print(f'{N}! = {mult}')