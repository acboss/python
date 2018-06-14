#1. Disegnare una curva di Koch di lunghezza x/3.
#2. Girare a sinistra di 60 gradi.
#3. Disegnare una curva di Koch di lunghezza x/3.
#4. Girare a destra di 120 gradi.
#5. Disegnare una curva di Koch di lunghezza x/3.
#6. Girare a sinistra di 60 gradi.
#7. Disegnare una curva di Koch di lunghezza x/3.
#Ad eccezione di quando x è minore di 3: in questo caso si disegna una linea dritta lunga x.


import turtle
bob = turtle.Turtle()

def koch1 (t, n):
    lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    t.fd(lunghezza)
    t.lt(angolo)
    koch1(t, lunghezza)
    t.rt(2*angolo)
    koch1(t, lunghezza)
    t.lt(angolo)
    t.fd(lunghezza)

def koch (t, n):
    lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    t.fd(lunghezza/3)
    t.lt(angolo)
    koch(t, lunghezza)
    t.rt(2*angolo)
    koch(t, lunghezza)
    t.lt(angolo)
    t.fd(lunghezza/3)

def koch2 (t,n):
    lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    t.fd(lunghezza/3)
    t.lt(angolo)
    koch(t, lunghezza/3)
    t.rt(2*angolo)
    koch(t, lunghezza/3)
    t.lt(angolo)
    t.fd(lunghezza/3)
    


koch (bob,500)


turtle.mainloop()