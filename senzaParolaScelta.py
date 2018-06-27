fin = open('words.txt')
def senzaLetteraScelta(parola,letteraScelta):
    i = 0
    lunghezza = (len(parola))-1
    while i <= lunghezza:
        a = parola[lunghezza]
        if ord(a) == ord(letteraScelta):
            return False
        else:
            lunghezza = lunghezza-1
    return True


def evitaLaLetteraScelta():
    for line in fin:
        parola = line.strip()
        if senzaLetteraScelta(parola,LetteraScelta):
            print(parola)

LetteraScelta = input()
evitaLaLetteraScelta()