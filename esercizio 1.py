import turtle
import math
def quadrato(t, lunghezza):
    for i in range(4):
        t.fd(lunghezza)
        t.lt(90)

def polilinea(t, n, lunghezza, angolo):
    for i in range(n):
        t.fd(lunghezza)
        t.lt(angolo)

def poligono(t, n, lunghezza):
    angolo = 360.0 / n
    polilinea(t, n, lunghezza, angolo)

def arco(t, r, angolo):
    arco_lunghezza = 2 * math.pi * r * angolo / 360
    n = int(arco_lunghezza / 3) + 1
    passo_lunghezza = arco_lunghezza / n
    passo_angolo = float(angolo) / n
    polilinea(t, n, passo_lunghezza, passo_angolo)

def cerchio(t, r):
    arco(t, r, 360)

bob = turtle.Turtle()










numeroLati = 6
raggio = 200
lunghezzaLato = 100
angoloArco = 90 

#quadrato(bob, lunghezzaLato)
#poligono(bob, numeroLati, lunghezzaLato)
#arco(bob, raggio, angoloArco)
cerchio(bob, raggio)

turtle.mainloop()