
def usaSolo(parola,lettere):
    i = 0
    lunghezza = (len(parola))-1
    while i < lunghezza:
        a = parola[lunghezza]
        if a in lettere:
            return True
        else:
            lunghezza = lunghezza-1
    return False



lettere = ['a','b']
print(usaSolo('ciao',lettere))

