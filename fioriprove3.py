import turtle
import math

def arco1(t, r, angolo):
    circonferenza = 2 * math.pi * r * angolo / 360
    n = int(circonferenza/ 3) + 1
    lunghezzaCerchio = circonferenza / n
    passo_angolo = float(angolo) / n
    for i in range(n):
        t.fd(lunghezzaCerchio)
        t.lt(passo_angolo)

def punto0(t,):
    t.pu()
    t.home()
    
    
def arco3(t, r, angolo):
    circonferenza = 2 * math.pi * r * angolo / 360
    n = int(circonferenza/ 3) + 1
    lunghezzaCerchio = circonferenza / n
    passo_angolo = float(angolo) / n  
    for i in range(n):
        t.pd()
        t.bk(lunghezzaCerchio)
        t.lt(passo_angolo)

def arco4(t, r, angolo):
    circonferenza = 2 * math.pi * r * angolo / 360
    n = int(circonferenza/ 3) + 1
    lunghezzaCerchio = circonferenza / n
    passo_angolo = float(angolo) / n
    for i in range(n):
        t.pd()
        t.fd(lunghezzaCerchio)
        t.rt(passo_angolo)

def arco5(t, r, angolo):
    circonferenza = 2 * math.pi * r * angolo / 360
    n = int(circonferenza/ 3) + 1
    lunghezzaCerchio = circonferenza / n
    passo_angolo = float(angolo) / n
    for i in range(n):
        t.pd()
        t.bk(lunghezzaCerchio)
        t.rt(passo_angolo)

def giro(t, r, angolo):
    circonferenza = 2 * math.pi * r * angolo / 360
    n = int(circonferenza/ 3) + 1
    lunghezzaCerchio = circonferenza / n
    passo_angolo = float(angolo) / n
    for i in range(n):
        t.pd()
        t.lt(passo_angolo)
        t.fd(lunghezzaCerchio)

 
    
    
    
    

bob = turtle.Turtle()

numeroLati = 6
raggio = 200
lunghezzaLato = 100
angoloArco = 90
angoloCheGira = 90
raggioCheGira = 0.1

arco1(bob, raggio, angoloArco)
punto0(bob)
arco3(bob, raggio, angoloArco)
punto0(bob)
arco4(bob, raggio, angoloArco)
punto0(bob)
arco5(bob, raggio, angoloArco)
giro(bob, raggioCheGira, angoloCheGira)

turtle.mainloop()