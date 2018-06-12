import time
import math

giorniDaConvertireInData = time.time()
secondiInUnGiorno = 86400
secondiInUnOra = 3600
secondiInUnMinuto = 60

def converti(daConvertire, convertitore):
    dato = daConvertire//convertitore
    resto = daConvertire%convertitore
    return dato, resto

giorni, restoGiorni = converti(giorniDaConvertireInData, secondiInUnGiorno)
ore, restoOre = converti(restoGiorni, secondiInUnOra)
minuti, secondi = converti(restoOre, secondiInUnMinuto)

print (str(int(giorni)) + " g  " + str(int(ore)) + " h  " + str(int(minuti)) + " min  " + str(int(secondi)) + " sec")
    

