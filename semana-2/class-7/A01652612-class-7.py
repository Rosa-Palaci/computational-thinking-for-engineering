#Class-7
#Rosa Vanessa Palacios Beltran
#A01652612

#Instrucciones

'''
#caso comillas
print(f'Pero \'supuestamente...')

print(f'Pero "supuestamente"...') #error

print(f"Pero 'supuestamente'...")
'''

#imprimir los numeros del 4 al 40, excepto el 7.

for num in range(4,41):
    if num == 7:
        continue

    print(num, end = ' ')

print('\n=======================')
num = 4
while num <= 40:
    if num == 7:
        continue
    print(num, end = ' ')
    num = num + 1