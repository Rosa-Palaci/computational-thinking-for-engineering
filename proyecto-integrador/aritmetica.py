import random as rm
import math as mt
#--------------------------------------------------------------------------

a = rm.randint(1,20)
b = rm.randint(1,20)
c = rm.randint(1,20)
d = rm.randint(1,20)
e = rm.randint(1,20)

g = rm.randint(1,20)
pr_art1 =(f"Cuanto es {a}+{b}+{c}?")
pr_art2 =(f"Cuanto es {a}+{b}·({c}+{d})-{b}·{a}+{c}?")
pr_art3 =(f"Cuanto es ({c}+{d})·({e}·{a})-{c}·{d}+{b}?")
pr_art4 =(f"Cuanto es {a}^2+{c}^2?")
pr_art5 =(f"Cuanto es ({c}+{d}·{a})/{e}?")
pr_art6 =(f"Cuanto es {a}^2+{c}·2-{d}·2?")
pr_art7 =(f"Cuanto es ({a}+{b})-({d}·{e})+{c}^2?")
pr_art8 =(f"Cuanto es la raiz de √{g}?")
pr_art9 =(f"Cuanto es {a}·({b}-({c}·{b}))+{g}·{a}?")
pr_art10 =(f"Cuanto es {g}·{d}+ √{g}-{e}^2?")
pr_art11 =(f"Cuanto es √{b} + {c}^2 +(√{d}+{g})?")
pr_art12 =(f"Cuanto es la raiz de {b}^4?")
pr_art13 =(f"Cuanto es ({a} +({b}/{d}))/{g}?")
r_art1 = a+b+c
r_art2 = a+b*(c+d)-b*a+c
r_art3 = (c+d)*(e*a)-c*d+b
r_art4 = a**2 +c**2
r_art5 = round((c+d*a)/(e),2)
r_art6 = a**2 +c*2-d*2
r_art7 = (a+b)-(d*e)+c**2
r_art8 = round(mt.sqrt(g),2)
r_art9 = a*(b-(c*b))+g*a
r_art10 = round(g*d+(mt.sqrt(g))-e**2,2)
r_art11 = round((round(b**(1/2),2))+c**2+(round((d+g)**(1/2),2)),2)
r_art12 = round(mt.sqrt(b**4))
r_art13 = round((a+(b/d))/g,2)
#-----------------------------------------------------------------------------------------
preguntas_arit =[pr_art1,pr_art2,pr_art3,pr_art4,pr_art5,pr_art6,pr_art7,pr_art8,pr_art9,pr_art10,pr_art11,pr_art12,pr_art13]
resp_arit =[r_art1,r_art2,r_art3,r_art4,r_art5,r_art6,r_art7,r_art8,r_art9,r_art10,r_art11,r_art12,r_art13]
#----------------------------------------------------------------------------------------
def pregunta_calif(pregunta,resp_cor,marcador):

    print(pregunta)
    print(resp_cor)
    resp = float(input('Respuesta: '))
    if resp == resp_cor:
        
        print('Correcto')
        marcador += 1
        correcto = print(f"Tu puntaje actual es de {marcador}\n")
        return marcador
        
    else:
        print('Incorrecto\n')
        incorrecto = print(f"Tu puntaje actual es de {marcador}\n")
        return marcador
puntaje_aritmetica = (f'Tu puntaje final de aritmetica {correcto}')
#------------------------------------------------------------
print("Preguntas de aritmetica")
print("En las respuestas que se necesite, ¡SOLO AGREGA 2 DECIMALES!\nDe igual manera solo usa dos decimales en la raices\nSi es necesario tambien redondea tu segunda decimal\nPor ejemplo: si tu resultado es 3.358, redondea a 3.36\n")

marc =0

for veces in range(13):
    
    pregArt = rm.choice(preguntas_arit)
    indice_preg = preguntas_arit.index(pregArt)
    marc=pregunta_calif(pregArt, resp_arit[indice_preg],marc)
    preguntas_arit.remove(pregArt)
    del resp_arit[indice_preg]