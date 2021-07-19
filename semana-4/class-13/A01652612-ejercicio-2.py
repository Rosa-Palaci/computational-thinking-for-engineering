#Actividad en clase - Datos Estructurados - Listas
#Rosa Vanessa Palacios Beltran
#A01652612

# Ejercicio 2
# El usuario deberá introducir mediante el teclado 
# sus 3 libros favoritos, los cuales deberás ir 
# guardando en una lista. 
# Al final, imprime la lista de libros.

listBooks = []
for pregunta in range(3):
    pregunta = input('Escriba uno de libros favoritos: ')
    listBooks.append(pregunta)
    #print(pregunta)
for list in listBooks:
    print(list)  
#print(listBooks)