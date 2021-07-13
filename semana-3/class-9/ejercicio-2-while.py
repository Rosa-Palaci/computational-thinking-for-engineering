#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 2

#Suma los números desde el 1 hasta el número entero 
# positivo capturado por el usuario y despliega el resultado de la suma.

# Por ejemplo:
# Si el número capturado es 10, deberás de mostrar:
# suma = 55

num = int(input('Digite un número entero positivo: '))
valorInicial = 1

print(f'Sumando los números desde {valorInicial} hasta {num}')

suma = (num*(num + 1))/2
print(f'suma = {suma}')  