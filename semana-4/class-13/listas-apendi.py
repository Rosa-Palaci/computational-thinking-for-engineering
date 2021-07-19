#Pide al usuario 6 números y guádarlos en una lista. Al final, imprimelos.

def imprimeLista(lista, simbolo):
    for elemento in lista:
        print(elemento, end = ' ')

        if elemento == [lista-1]: #Que representa el i
            print(elemento)
    print()

listaNum = []

for veces in range(6):
    num =float(input("Teclea un númmero"))
    listaNum.apped(num)
