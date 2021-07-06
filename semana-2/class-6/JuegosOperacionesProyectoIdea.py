#Muestra al usuario 5 operaciones de suma al azar. Cada respuesta 
# correcta le da 5 puntos. cada respuesta incorrecta le resta 1 punto. 
# Al final, muestra el puntaje total.

import random
 
num1= random.randint(0,20)
num2= random.randint(0,20)
resp1 = int(input(f'Calcula la siguiente suma: {num1} + {num2} = '))
resp_correcta = 