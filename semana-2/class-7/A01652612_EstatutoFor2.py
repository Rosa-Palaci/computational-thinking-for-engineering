#Actividad en clase - Estatuto for y los rangos - 1
#Rosa Vanessa Palacios Beltran
#A01652612

# Ejercicio # 1

cant_num = int(input('¿Cuántos números deseas ingresar?: '))
suma = 0
for veces in range(cant_num):
    num = float(input('Introduce un número: '))
    suma = suma + num

#print(suma)
promedio = suma/cant_num

print(f'El promedio de los números es {promedio}')


#Ejercicio # 2
#Cuenta de inversión: 

#En una cuenta de inversión, a principios del año 2020, 
# el saldo era de 100,500 pesos. El banco da un rendimiento 
# de 8% de interés anual, donde cada mes el porcentaje de 
# interés calculado se acumula al saldo de la cuenta, es 
# decir, cada mes el saldo de la cuenta al final del mes, 
# es igual al saldo en ese momento, más el cálculo 
# del interés mensual. 

#En el mes de julio se va hacer un retiro por 90,500 pesos. 

#Y el mes de octubre se va hacer un depósito por 50,000 pesos. 

#Utiliza la función For para calcular y desplegar cuánto va 
# a ser el saldo de la cuenta al final del año.

