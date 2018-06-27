

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