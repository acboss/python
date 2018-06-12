import turtle
import math

def quadrato(t,lunghezza):
    for i in range(4):
        bob.fd(lunghezza)
        bob.lt(90)

def poligono(t, lunghezza, n):
    for i in range(n):
        bob.fd(lunghezza)
        bob.lt(360/n)

def cerchio(t, r):
    nc = 160
    circonferenza = math.pi*r
    lunghezzaCerchio = circonferenza/nc
    poligono(t, lunghezzaCerchio, nc)

def arco(t, r, angolo):
    nc = 160 #numero lati circonferenza
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

quadrato(bob, lunghezzaLato)
poligono(bob, lunghezzaLato, n)
cerchio(bob, r)
arco(bob,r, angoloArco)
turtle.mainloop()