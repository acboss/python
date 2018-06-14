
import turtle
bob = turtle.Turtle()

def koch1(t,n):
    lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    t.fd(lunghezza)
    t.lt(angolo)

    t.fd(lunghezza)
    t.rt(angolo*2)

    t.fd(lunghezza)
    t.lt(angolo)

    t.fd(lunghezza)

def koch2(t,n):
    lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    koch1(t,lunghezza)
    t.lt(angolo)

    koch1(t,lunghezza)
    t.rt(angolo*2)

    koch1(t,lunghezza)
    t.lt(angolo)

    koch1(t,lunghezza)

def koch(t,n):
        lunghezza = n/3
    if not (n>=3):
        t.fd(n)
        return
    angolo = 60
    koch2(t,lunghezza)
    t.lt(angolo)

    koch2(t,lunghezza)
    t.rt(angolo*2)

    koch2(t,lunghezza)
    t.lt(angolo)

    koch2(t,lunghezza)




koch (bob,500)


turtle.mainloop()