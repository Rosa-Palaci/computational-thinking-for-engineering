#Actividad en clase - Estatuto while - 2
#Rosa Vanessa Palacios Beltran
#A01652612

#Ejercicio 7

'''
Muestra en pantalla n caracteres que alternan entre # y %, donde n es un número entero capturado por el usuario.
Los caracteres se deben mostrar uno en cada renglón.
Observa que el primer caracter que se debe mostrar siempre es #

Por ejemplo:
Si n = 5, deberás de mostrar:
#
%
#
%
#
'''
n = int(input('Introduce \'n\': '))
for veces in range(n):
    res = veces%2
    if res == 0: #Significa que 'veces' es par
        print('#')
    else:
        print('%')