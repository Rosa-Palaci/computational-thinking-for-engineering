#Crea un archivo llamado texto.txt y agrega tu nombre.
#Al final, cierra el archivo.

#Apertura del archivo
nom_arch = 'texto.txt'
arch = open(nom_arch, 'a')

#Escritura del archivo
arch.write('Manuel\n')
arch.write('Casillas\n')

#Cerrando el archivo.
arch.close()
