#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 1
suma = 0
num = int(input('Introduce un número entero: '))
suma = suma + num
print(f'Suma: {suma}')

while suma != 0:
    num =int(input('Introduce un número entero: '))
    suma = suma + num #Forma equivalente sum += num
    print(f'Suma + {suma}\n')

print('Programa finalizado')