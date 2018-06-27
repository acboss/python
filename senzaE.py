

fin = open('http://greenteapress.com/thinkpython2/code/words.txt')
for riga in fin:
    parola = riga.strip()
    lunghezza = (len(parola))-1
    while lunghezza > -1:
        a = testo[lunghezza] 
        if a == 'e' or a == 'E':
            print('')
        elif lunghezza == -1:
            print(parola)