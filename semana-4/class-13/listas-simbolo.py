#Pide al usuario 6 números y guárdalos en una 
# lista. Al final, imprimelos.

def imprimeLista(lista, simbolo):
    for elemento in lista:
        if elemento == lista[-1]:#Que representa el último elemento.
            print(elemento)
    
        else:
            print(elemento, end = simbolo)
    print()

listaNumeros = []

for veces in range(6):
    num = float(input("Teclea un númmero: "))
    listaNumeros.append(num)

imprimeLista(listaNumeros, ', ')