def di_x():
    print ('+', end=' ') 

def per_le_meno(): 
    print ('-', end=' ')
    print ('-', end=' ')
    print ('-', end=' ')
    print ('-', end=' ')

def primo_pezzo():
    di_x()
    per_le_meno()

def due_pezzi():
    primo_pezzo()
    primo_pezzo()

def prima_riga():
    due_pezzi()
    print('+')
    print()

def simbolo():
    print('|', end=' ')

def spazi():
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
 
def primo_pezzo_riga_2():
    simbolo()
    spazi()

def due_pezzi_riga_2():
    primo_pezzo_riga_2()
    primo_pezzo_riga_2()

def seconda_riga():
    due_pezzi_riga_2()
    print('|')
    print()

def mezzo():
    seconda_riga()
    seconda_riga()
    seconda_riga()
    seconda_riga()

def tutto():
    prima_riga()
    mezzo()
    prima_riga()
    mezzo()
    prima_riga()

tutto()