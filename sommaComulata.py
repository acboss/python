def somma_comulata(numeri):
    totale = 0
    sommaComulata = []
    for x in numeri:
        totale += x
        sommaComulata.append(totale)
    return sommaComulata

numeri = [1,2,3]
print(somma_comulata(numeri))