#Clase-8
#Rosa Vanessa Palacios Beltran
#A01652612

#Instrucciones

#Formula una pregunta de opcion múltiple al usuario.
#Mientras la respuesta sea incorrecta, sigue haciendo la misma pregunta.

print('¿Quién escribió el libro de Azteca?')
print('a)Crevantes \tb)Stepshen King \tc)Gary Jennings \td)Octavio Paz')
resp = input('Teclea tu respuesta: ')

while resp != 'c':
    resp = input('Repsuesta incorrecta, vuelve a intentarlo: ')

print('Respuesta correcta')

