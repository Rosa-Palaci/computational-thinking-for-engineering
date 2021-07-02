#Actividad - Programas que usan estatutos de decisión con operaciones aritméticas
#IMC
#Rosa Vanessa Palacios Beltran
#A01652612

#Calcule el índice de masa corporal (IMC)

import math

peso = float(input('Ingresa tu peso (kg): ' ))
if peso <= 0.499:
    print('Peso no valido')
    quit()
elif peso >= 650:
    print('Peso no valido, verifica que este en kilogramos')
    quit()

altura = float(input('Ingresa tu altura (m): '))

if altura <= 0.2:
    print('La altura no es valida')
    quit()
elif altura >= 2.5:
    print('La altura no es valida, verifica que este en metros')
    quit()    
else:
    print

IMC = peso / (altura**2)

if IMC < 20:
    categoria = 'Peso bajo'
elif 20 <= IMC < 25:
    categoria = 'Peso normal'
elif 25 <= IMC < 30:
    categoria = 'Sobrepeso'
elif 30 <= IMC < 40:
    categoria = 'Obesidad'

print(f'Su Indice de Masa Corporal es {IMC}, lo que muestra que su peso está en la categoría de {categoria} ')