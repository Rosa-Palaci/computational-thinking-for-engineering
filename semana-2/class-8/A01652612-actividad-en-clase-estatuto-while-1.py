#Actividad en clase - Estatuto while - 1
#Rosa Vanessa Palacios Beltran
#A01652612

#Instrucciones

# Ejercicio 1 
# ¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:

x = 8
y = 3
while y <= 16:
    x += 1
    y += 2

print(x)
print(y)

# Ejercicio 2 
# ¿Qué aparece en la pantalla si se ejecuta el siguiente código de Python?:

d = 0
r = 13
s = r / 2
while s > 2 or r % 2 == 0:
    d += 1     
    r -= 2     
    s -= 2

print(str(d) + " " + str(r) + " " + str(s))