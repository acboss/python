
def ciSono(parola,lettere):
    i = 0
    lunghezza = (len(parola))-1
    while i < lunghezza:
        a = parola[lunghezza]
        if a in lettere:
            return True
            lunghezza = lunghezza-1
    return False

def usaSolo(parola,lettere):
    if ciSono(parola,lettere) == True:
        if parola in lettere:
            return True
        else:
            return False


lettere = ['s']
print(ciSono('ciao',lettere))
print(usaSolo('ciao',lettere))

