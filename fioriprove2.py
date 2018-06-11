import turtle
import math

  
def dati(raggio, angolo):
    circonferenza = 2 * math.pi * raggio * angolo / 360
    numeroLati = int(circonferenza/ 7) + 1
    lunghezzaCerchio = circonferenza / numeroLati
    passo_angolo = float(angolo) / numeroLati
    return lunghezzaCerchio, passo_angolo, numeroLati

def arco(t, raggio, angolo):
    lunghezzaCerchio, passo_angolo, numeroLati = dati(raggio, angolo)
    for i in range(numeroLati):
        t.fd(lunghezzaCerchio)
        t.lt(passo_angolo)



def giro(t, raggio, angolo):
    lunghezzaCerchio, passo_angolo, numeroLati = dati(raggio, angolo)
    for i in range(numeroLati):
        t.pd()
        t.lt(passo_angolo)
        t.fd(lunghezzaCerchio)

def fiore(t, raggio, numeroPetali, angoloArco, angoloArco2):
    angoloCheGira = 360/NumeroPetali 
    raggioCheGira = 00.0000001      #0.01
    arco(t, raggio, angoloArco)     
    for i in range(numeroPetali):
       giro(t, raggioCheGira, angoloCheGira)
       arco(t, raggio, angoloArco2) 

NumeroPetali = 4
Bob = turtle.Turtle()

AngoloArco2 = 720/NumeroPetali   #180
AngoloArco = 360/NumeroPetali   #90
Raggio = 200  #influisce sulla dimensione del fiore

 
fiore(Bob, Raggio, NumeroPetali, AngoloArco, AngoloArco2)