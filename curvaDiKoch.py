import turtle
bob = turtle.Turtle()
bob.speed(0)

def dati(t,n):
    lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    return angolo, n, lunghezza

def koch1(t,n):
    angolo, n, lunghezza = dati(t,n)
    t.fd(lunghezza)
    t.lt(angolo)

    t.fd(lunghezza)
    t.rt(angolo*2)

    t.fd(lunghezza)
    t.lt(angolo)

    t.fd(lunghezza)

def koch2(t,n):
    angolo, n, lunghezza = dati(t,n)
    koch1(t,lunghezza)
    t.lt(angolo)

    koch1(t,lunghezza)
    t.rt(angolo*2)

    koch1(t,lunghezza)
    t.lt(angolo)

    koch1(t,lunghezza)

def koch3(t,n):
    angolo, n, lunghezza = dati(t,n)
    koch2(t,lunghezza)
    t.lt(angolo)

    koch2(t,lunghezza)
    t.rt(angolo*2)

    koch2(t,lunghezza)
    t.lt(angolo)

    koch2(t,lunghezza)

def koch4(t,n):
    angolo, n, lunghezza = dati(t,n)
    koch3(t,lunghezza)
    t.lt(angolo)

    koch3(t,lunghezza)
    t.rt(angolo*2)

    koch3(t,lunghezza)
    t.lt(angolo)

    koch3(t,lunghezza)

def koch5(t,n):
    angolo, n, lunghezza = dati(t,n)
    koch4(t,lunghezza)
    t.lt(angolo)

    koch4(t,lunghezza)
    t.rt(angolo*2)

    koch4(t,lunghezza)
    t.lt(angolo)

    koch4(t,lunghezza)

def fioccoDiNeve(t,lunghezza):
    koch5 (t,lunghezza)
    t.rt(120)
    koch5 (t,lunghezza)
    t.rt(120)
    koch5 (t,lunghezza)

Lunghezza = 500

fioccoDiNeve(bob, Lunghezza)


turtle.mainloop()