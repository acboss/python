fin = open('words.txt')



def maggioreDiVenti(parola):
    lunghezza = len(parola)
    if lunghezza >= 20:
        return True
    else:
        return False


def trovaMaggioreDiVenti():
    for line in fin:
        parola = line.strip()
        if maggioreDiVenti(parola):
            print(parola)

trovaMaggioreDiVenti()