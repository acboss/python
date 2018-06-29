import random

def ha_duplicati(t):
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def compleanniCasuali(n):
    t = []
    for i in range(n):
        compleanni = random.randint(1, 365)
        t.append(compleanni)
    return t

def trovaCompleanniUguali(numeroStudenti, numeroSimulazioni):
    conta = 0
    for i in range(numeroSimulazioni):
        t = compleanniCasuali(numeroStudenti)
        if ha_duplicati(t):
            conta += 1
    return conta



numeroStudenti = 23
numeroSimulazioni= 1000
conta = trovaCompleanniUguali(numeroStudenti, numeroSimulazioni)
print('compleanni uguali contati ' + str(conta))