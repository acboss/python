

def trovaLeE():
    for line in fin:
    parola = line.strip()
        if usaSolo(parola,lettera(Lettere)):
            print(parola)

def lettera(lettere)
    if len(lettere) >= 1:
        i = 0
        lunghezzaLettere = (len(lettere))-1
        while i < lunghezzaLettere:
            al = lettera[lunghezzaLettere] 
            return letteraSingola = al 
            lunghezza = lunghezza-1


def usaSolo(parola,letteraSingola):
    i = 0
    lunghezza = (len(parola))-1
    while i < lunghezza:
        a = parola[lunghezza]
        if ord(a) == ord(letteraSingola)
            return True
        else:
            lunghezza = lunghezza-1
    return False



Lettere = input()
print(trovaLeE(ciao,lettere))

