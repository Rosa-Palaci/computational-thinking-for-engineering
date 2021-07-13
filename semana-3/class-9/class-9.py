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

# Ejercicio 2

n = int(input('Digite un número entero positivo: '))
valorInicial = 1

print(f'Lista de ({valorInicial} a {n}) de uno en uno')

for listaCrece in range(valorInicial,n + 1,1):
    if listaCrece == n:
        print(listaCrece, end='\n')
    else:
        print(listaCrece, end = ', ')
    
print(f'\nLista de ({n} a {valorInicial}) de menos uno en menos uno')
if n >= valorInicial:
    for listaDecrece in range(n,0,-1):
        if listaDecrece == valorInicial:
            print(listaDecrece, end='\n')
        else:
            print(listaDecrece, end = ', ')

# Ejercicio 3
# Pide al usuario un número entero positivo, 
# calcula la suma de los números al cuadraado y muestro el resultado.

num_final = int(input('Introduce el número final: '))
suma_3 = 0
for num3 in range(1, num_final + 1):
    suma_3 = suma_3 + num3**2 #Equivalente a suma_3 += num3

print(f'La suma desde 1^2 hasta {num_final}^2 es {suma} ')