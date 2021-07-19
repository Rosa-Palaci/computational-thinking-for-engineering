#Actividad en clase - Datos Estructurados - Listas
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 2

#El usuario deberá introducir mediante el 
# teclado sus 3 libros favoritos, los cuales 
# deberás ir guardando en una lista. 
# Al final, imprime la lista de libros.

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
