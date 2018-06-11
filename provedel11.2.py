import time
tempo = time.time()

def sec(t):
    print('sec'+ str((t%60)*60))
def minuti(t):
    min = t//60
    print('min'+ str(((min%60)*60)+min))
    return min
def ore(t):
    min = minuti(t)
    h = min//60
    print('min'+ str(((h%24)*60)+h))
    return h
def giorni(t):
    h = ore(t)
    print ('h'+ str(h//24))

sec(tempo)
minuti(tempo)
ore(tempo)
giorni(tempo)

    

