import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else: #Sistema operativo MAC OSX
        subprocess.call(['open', filename])
        
print('1) Imagen\n2) Sonido\n3) Video')
opc = int(input('¿Qué archivo quieres abrir?: '))
if opc == 1:
    nom_arch = 'hugepizza.png'
elif opc == 2:
    nom_arch = 'music.mp3'
elif opc == 3:
    nom_arch = 'video.mp4'
else:
    nom_arch = ''
    
open_file(nom_arch)