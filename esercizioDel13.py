#Leggete la seguente funzione e cercate di capire cosa fa. Quindi eseguitela per controllare se avevate indovinato.

import turtle
bob = turtle.Turtle()

def disegna(t, lunghezza, n):
    if n == 0:
        return
    angolo = 50
    t.fd(lunghezza*n)
    t.lt(angolo)
    disegna(t, lunghezza, n-1)
    t.rt(2*angolo)
    disegna(t, lunghezza, n-1)
    t.lt(angolo)
    t.bk(lunghezza*n)


disegna (bob,2,5)

turtle.mainloop()