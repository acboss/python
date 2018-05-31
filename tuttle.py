import turtle
import math

  
def dati(raggio, angolo):
    circonferenza = 2 * math.pi * raggio * angolo / 360
    numeroLati = int(circonferenza/ 7) + 1
    lunghezzaCerchio = circonferenza / numeroLati
    passo_angolo = float(angolo) / numeroLati
    return lunghezzaCerchio, passo_angolo, numeroLati

def arco(t, raggio, angolo, lunghezzaCerchio_prova):
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
    angoloCheGira = 90                #360/NumeroPetali 
    raggioCheGira = 00.0000001      #0.01
    arco(t, raggio, angoloArco, lunghezzaChercio_prova)     #la prova e' da eliminare non sostituire 
    for i in range(numeroPetali):
       giro(t, raggioCheGira, angoloCheGira)
       arco(t, raggio, angoloArco2) 

Bob = turtle.Turtle()
NumeroPetali = Numeratore/Denominatore
p = Raggio*math.sin(NumeroPetali*O)
P2 = Raggio*math.sin(NumeroPetali*O2)
x = p*math.cos(O)
y = p*math.sin(O)
x1 = p*math.cos(O2)
y1 = p*mat.sin(O2)
P = math.sqrt(x*x + y*y)
p2 = math.sqrt(x1*x1 + y1*y1)
Numeratore = 
Denominatore =
lunghezzaCerchio_prova = (2*math.pi*Raggio*O)/360      #Formula per sapere la lunghezza di un pezzo di cerchio (t.fd)    lunghezzaCerchio
lunghezzaCerchio_prova2 = (2*math.pi*Raggio*O2)/360
O = angoloArco
O2 = angoloArco2

angoloArco2 = 180          #720/numeroPetali   #180
angoloArco = 90            #360/numeroPetali   #90
Raggio = 200  #influisce sulla dimensione del fiore



fiore(Bob, Raggio, NumeroPetali, AngoloArco, AngoloArco2)

#giro(bob,raggioCheGira, angoloCheGira)
#arco(bob, raggio, angoloArco2)
#giro(bob,raggioCheGira, angoloCheGira)
#arco(bob, raggio, angoloArco2)
#giro(bob,raggioCheGira, angoloCheGira)
#arco(bob, raggio, angoloArco)


turtle.mainloop()