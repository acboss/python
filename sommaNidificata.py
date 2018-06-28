def somma_nidificata(numeri):
    totale = 0
    for nidificata in numeri:
        totale += sum(nidificata)
    return totale

numeri = [[1, 2], [3], [4, 5, 6]]
print(somma_nidificata(numeri))