import turtle
import math

def dati(raggio, angolo):
    circonferenza = 2 * math.pi * raggio * angolo / 360
    numeroLati = int(circonferenza/ 7) + 1
    lunghezzaCerchio = circonferenza / numeroLati
    passo_angolo = float(angolo) / numeroLati
    return lunghezzaCerchio, passo_angolo, numeroLati


def dati2(raggio, angolo2):
    circonferenza2 = 2 * math.pi * raggio * angolo2 / 360
    numeroLati2 = int(circonferenza2/ 7) + 1
    lunghezzaCerchio2 = circonferenza2 / numeroLati2
    passo_angolo2 = float(angolo2) / numeroLati2
    return lunghezzaCerchio2, passo_angolo2, numeroLati2


def An(t, raggio, angolo, angolo2):
    def giroA(t, raggio, angolo):
        lunghezzaCerchio, passo_angolo, numeroLati = dati(raggio, angolo)
        for i in range(numeroLati):
            t.pd()
            t.lt(passo_angolo)
            t.fd(lunghezzaCerchio)
    def giroA2(t, raggio, angolo2):
        lunghezzaCerchio2, passo_angolo2, numeroLati2 = dati2(raggio, angolo2)
        for i in range(numeroLati2):
            t.pd()
            t.rt(passo_angolo2)
            t.fd(lunghezzaCerchio2)
    giroA(t, raggio, angolo)
    t.fd(100)
    giroA2(t, raggio, angolo2)
    t.fd(100)






Raggio  = 0.0000001
Angolo= 60
Angolo2 = 90
Bob = turtle.Turtle()

An(Bob, Raggio, Angolo, Angolo2)

turtle.mainloop()


