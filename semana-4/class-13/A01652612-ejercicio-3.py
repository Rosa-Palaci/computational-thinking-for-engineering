#Actividad en clase - Datos Estructurados - Listas
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 3

#Crea una lista que simule las calificaciones 
# de 10 actividades de un alumno. Supón que 
# debido al excepcional desempeño del alumno, 
# el profesor ha decidido aumentar 5 puntos.
# Tu programa deberá aumentar a cada calificación 
# los 5 puntos (recordando que la calificación 
# máxima es de 100 y no puede pasarse)

califs = [100, 90, 45, 67, 12, 99, 80, 40, 60, 100]
nueva_calif = []

for calif in califs:
    if calif + 5 > 100:
        calif = 100
    else:
        calif += 5
    
    nueva_calif.append(calif)

print(califs)
print(nueva_calif)