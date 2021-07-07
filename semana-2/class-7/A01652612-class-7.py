#Class-7
#Rosa Vanessa Palacios Beltran
#A01652612

'''caso comillas
print(f'Pero \'supuestamente...')
print(f'Pero "supuestamente"...') error
print(f"Pero 'supuestamente'...") 

#imprimir los numeros del 4 al 40, excepto el 5.
for num in range(4,41):
    residuo = num%5
    if residuo == 0:#Significa que es multiplo de 5
        continue

    print(num, end = ' ')'''

#Pide al usuario o números, pero si ingresa un 7 
# ya no se pide más números.

for veces in range (6):
    num = int(input('Introcue un número: '))

    if num == 7:
        print('El programa va a terminar')
        break
print('Espero que tengas un buen día')
