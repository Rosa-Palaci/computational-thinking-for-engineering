#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 3

# Pide al usuario un número entero positivo, 
# calcula la suma de los números al cuadraado y muestro el resultado.

num_final = int(input('Introduce el número final: '))
suma_3 = 0
for num3 in range(1, num_final + 1):
    suma_3 = suma_3 + num3**2 #Equivalente a suma_3 += num3

print(f'La suma desde 1^2 hasta {num_final}^2 es {suma} ')