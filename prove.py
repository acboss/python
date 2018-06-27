fin = open('words.txt')
fin.readline() #legge una riga e va a capo se si riscrive legge la riga successiva e va a capo e così via


riga = fin.readline()
parola = riga.strip()
parola #se si vuole togliere lo \n

fin = open('words.txt')
for riga in fin:
    parola = riga.strip()
    print(parola) #stampa tutte le parole una per riga
