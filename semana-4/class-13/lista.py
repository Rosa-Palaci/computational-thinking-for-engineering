#Pide al usuario 6 números y guárdalos 
# en una lista. Al final, imprimelos.

def imprimeLista(lista):
    for elemento in lista:
        print(elemento, end = ' ')
    print()

listaNumeros = []
num = input('Teclea un número: ')
listaNumeros.append(num)
imprimeLista(listaNumeros)

num = float(input('Teclea un número: '))
listaNumeros.append(num)
imprimeLista(listaNumeros)