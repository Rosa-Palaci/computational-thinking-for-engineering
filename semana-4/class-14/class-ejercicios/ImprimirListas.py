#Función para imprimir listas (por default el símbolo delimitador es la coma) 
def imprime_lista(lista, simbolo = ', '):
    i = 0
    for elemento in lista:
        if i == len(lista) - 1: #representa el índice del último elemento.
            print(elemento, end = '')
        else:
            print(elemento, end = simbolo)
        i += 1
    print()