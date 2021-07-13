#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 2

#Suma los números desde el 1 hasta el número entero positivo capturado por el usuario y despliega el resultado de la suma.

# Por ejemplo:
# Si el número capturado es 10, deberás de mostrar:

suma = 55

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