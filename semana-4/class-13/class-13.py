# Define una función que reciba una lista e imprima cada elemento, separado por un espacio.
# Crea dos listas e imprimelas con tu función.

def imprimeLista(lista):
    for elemento in lista:
        print(elemento, end =' ')
    print()

listaElementos = [20, 'Palabra', 'x', -12.35, 2*3 + 1]
listaLibros = ['Azteca', "Crimen y Castigo"]

imprimeLista(listaElementos)
imprimeLista(listaLibros)