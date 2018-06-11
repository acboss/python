import time
time.time()
def giorni():
    print (time.time()//24)
def ore():
    h = time.time()%24
    priint (h//60)
    return h
def minuti():
    h = ore()
    min = (h%60)//60
    print (min)
    return min
def secondi():
    min//