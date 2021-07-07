#Actividad en clase - Estatuto for y los rangos - 1
#Rosa Vanessa Palacios Beltran
#A01652612

# Ejercicio # 1 - proemdio

cant_num = int(input('¿Cuántos números deseas ingresar?: '))
suma = 0
for veces in range(cant_num):
    num = float(input('Introduce un número: '))
    suma = suma + num

#print(suma)
promedio = suma/cant_num

print(f'El promedio de los números es {promedio}')


#Ejercicio # 2 - Cuenta de inversión: 

saldo = 100500
interes = 0.08/12

for meses in range(1,13):
    if meses == 7: 
        saldo = saldo - 90500

    elif meses == 10: 
        saldo = saldo + 50000

    saldo = saldo + saldo*interes
    #print(f'{meses}: ${saldo:.2f}')

print(f'El salfo final es de ${saldo:.2f}')