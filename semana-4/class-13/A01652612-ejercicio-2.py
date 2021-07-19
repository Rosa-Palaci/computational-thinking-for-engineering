#Actividad en clase - Datos Estructurados - Listas
#Rosa Vanessa Palacios Beltran
#A01652612

# Ejercicio 1
# Crea una lista con el nombre de 5 personas 
# que más admires. Imprime cada elemento de la 
# lista mediante un ciclo for.

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