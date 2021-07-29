#Crea una lista de listas

def imprimir_tabla(alumnos):
    print()
    print('Nombre Matrícula Semestre Promedio')
    print('---------------------------')
    for registro in alumnos:
        for elemento in registro:
            print(elemento, end = '|')
        print()
    print('---------------------------')
    print()

alumnos = [ ['Jorge', 'A012345', 3, 82], ['Laura', 'A200423', 4, 95]]

#Imprimir cada registro

imprimir_tabla(alumnos)

#Pide al usuario que introduzca la información de dos alumnos más.

opc = ''
while opc != 'N':
#for veces in range(2):
    alumno = []
    nom = input('Teclea el nombre (X para finalizar): ')
    mat = input('Teclea la matrícula: ')
    sem = int(input('Teclea el semestre: '))
    prom = float(input('Teclea el promedio actual: '))
    alumno.append(nom)
    alumno.append(mat)
    alumno.append(sem)
    alumno.append(prom)
        
    alumnos.append(alumno)
    
    opc = input('¿Desea introducir otro registro? (S/N): ')

imprimir_tabla(alumnos)

    
    
    
    
    
    