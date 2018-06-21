import math

def !(n):
    if n == 0:
        n = 1
        return n
    else:
        fine = n*(!(n-1))
        return fine



def stima_pi():
    while True:
        num1 = 2*math.sqrt(2)
        den1 = 9801
        num2 = (!(4*k))*(1103+26390*k)
        dem2 = (!(k)**4)*(396**(4*k))
        uno = num1/den1
        due = num2/den2
        equazione = uno*due
        totale += equazione
        if n(equazione) < 1e-15:
            break
        k += 1
    return 1/totale

print(stima_pi())