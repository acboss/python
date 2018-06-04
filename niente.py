import turtle
import math
bob = turtle.Turtle()

def dati(raggio, angolo):
    circonferenza = 2 * math.pi * raggio * angolo / 360
    numeroLati = int(circonferenza/ 7) + 1
    lunghezzaCerchio = circonferenza / numeroLati
    passo_angolo = float(angolo) / numeroLati
    return lunghezzaCerchio, passo_angolo, numeroLati



def giro(t, raggio, angolo):
    lunghezzaCerchio, passo_angolo, numeroLati = dati(raggio, angolo)
    for i in range(numeroLati):
        t.pd()
        t.lt(passo_angolo)
        t.fd(lunghezzaCerchio)

def giro2(t, raggio, angolo):
    lunghezzaCerchio, passo_angolo, numeroLati = dati(raggio, angolo)
    for i in range(numeroLati):
        t.pd()
        t.rt(passo_angolo)
        t.fd(lunghezzaCerchio)

AngoloArco = 180
Raggio1 = 33
Raggio2 = 16
giro(bob, Raggio1, AngoloArco)
giro2(bob, Raggio2, AngoloArco)






turtle.mainloop()