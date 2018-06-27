

fin = open('words.txt')
riga = fin.readline()
for riga in fin:
    parola = riga.strip()
    lunghezza = (len(parola))-1
    while lunghezza > -1:
        a = riga[lunghezza] 
        if a == 'e' or a == 'E':
            print('')
        elif lunghezza == -1:
            print(parola)
def senzaE(parola):
    i = 0
    lunghezza = (len(parola))-1
    while i < lunghezza:
        a = riga[lunghezza]
        if ord(a) == 69 or ord(a) == 101:
            return False
            
        else:
            return True
        lunghezza = lunghezza-1
        if lunghezza == -1:
            break

def trovaLeE():

    fin = open('words.txt')
    for line in fin:
        parola = line.strip()
        if senzaE(parola):
            print(parola)

trovaLeE()