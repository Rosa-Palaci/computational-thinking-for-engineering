#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 3

# Pide al usuario un número entero positivo, 
# calcula la suma de los números al cuadrado y muestro el resultado.


numFinal = int(input('Ingresa un número entero positivo final: '))
suma = 0
for num in range(1, numFinal + 1):
    suma = suma + num**2 

print(f'La suma es desde 1^2 hasta {numFinal}^2 es {suma} ')