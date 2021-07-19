#Pide al usuario 6 números y guádarlos en una lista. Al final, imprimelos.

def imprimeLista(lista):
    for elemento in lista:
        print(elemento, end = ' ')
    print()

listaNum = []

for veces in range(6):
    num =float(input("Teclea un númmero"))
    listaNum.apped(num)

imprimeLista(listaNum)