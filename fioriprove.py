import turtle
import math

def arco(t, r, angolo):
    nc = int(circonferenza/ 3) + 1 #numero lati circonferenza
    angoloGiro = 360
    circonferenza = 2*math.pi*r*angolo/angoloGiro
    lunghezzaCerchio = circonferenza/nc
    numeroArchiPerCirconferenza = angoloGiro/angoloArco
    numeroLatiArco = nc/numeroArchiPerCirconferenza
    for i in range(numeroLatiArco):
        bob.fd(lunghezzaLato)
        bob.lt(angoloArco/numeroLatiArco)

bob = turtle.Turtle()
print(bob)
#bob.down()
lunghezzaLato = 100
n = 6 #Numero lati
r = 200
angoloArco = 90

arco(bob,r, angoloArco)
turtle.mainloop()