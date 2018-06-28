fin = open('words.txt')


def senzaE(parola):
    i = 0
    lunghezza = (len(parola))-1
    while i <= lunghezza:
        a = parola[lunghezza]
        if ord(a) == 69 or ord(a) == 101:
            return False
        else:
            lunghezza = lunghezza-1

    return True


def trovaLeE():


    for line in fin:
        parola = line.strip()
        if senzaE(parola):
            print(parola)


trovaLeE()