#Actividad en clase - Estatuto for y los rangos - 1
#Rosa Vanessa Palacios Beltran
#A01652612

#Instrucciones 
'''
Escribe un programa que lea un número entero positivo n 
 y muestre una lista de números que empieza en 1 e 
 incrementa de uno en uno hasta llegar a n y después 
 decrementa de uno en uno hasta llegar a 1:
# 1, 2, ... n, n-1, n-2 ... 1
'''

#numEntero 

n = int(input('Digite un número entero pisitivo: '))
valorInicial = 1

print(f'\n Lista de ({valorInicial} a {n}) de uno en uno')

for listaCrece in range(valorInicial,n + 1,1):
    print(listaCrece, end = ', ')

valorFinal = 1

print(f'\n Lista de ({n} a {valorFinal}) de menos uno en menos uno')
if n > valorFinal:
    for listaDecrece in range(n,valorFinal-1,-1):
        print(listaDecrece, end = ', ')