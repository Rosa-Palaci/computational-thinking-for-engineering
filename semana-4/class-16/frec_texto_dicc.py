#Haz un programa que, dado un texto, realice el conteo de las frecuencias de cada caracter
#Por ejemplo, si el texto es 'Esto es una prueba!'
#Se debe de obtener lo siguiente
'''
E : 1
s : 2
t : 1
o : 1
  : 3
e : 2
u : 2
n : 1
a : 2
p : 1
r : 1
b : 1
! : 1
'''

frecuencias = {}
texto = 'aaabbbccddeeeee'
for car in texto:
    #Revisar si la llave (car) está en el diccionario
    if car in frecuencias:
        frecuencias[car] += 1
    else: #Si no existe, se agrega al diccionario
        frecuencias[car] = 1

print(texto)
for car in frecuencias:
    print(f'{car} : {frecuencias[car]}')
    
    
    
    
    
    
    
    
    
    
