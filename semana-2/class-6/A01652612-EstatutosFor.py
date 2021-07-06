#Actividad en clase - Estatuto for y los rangos - 1
#Rosa Vanessa Palacios Beltran
#A01652612
'''
Instrucciones 
Escribe un programa que lea un número entero positivo n 
 y muestre una lista de números que empieza en 1 e 
 incrementa de uno en uno hasta llegar a n y después 
 decrementa de uno en uno hasta llegar a 1:
# 1, 2, ... n, n-1, n-2 ... 1
'''
n = int(input('Digite un número entero pisitivo: '))
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
            print(listaDecrece, end = ', ') #18 lineas