def prima(parola):
    return parola[0]
def ultima(parola):
    return parola[-1]
def mezzo(parola):
    return parola[1:-1]

def palidromo(parola):
    if len(parola) <= 1:
        return True
    if prima(parola) != ultima(parola):
        return False
    return palidromo(mezzo(parola))


# ho aggiunto una stringa a ciò che stampi in modo che si capisca meglio quali parole hai analizzato per vedere se sono palindrome o meno
print("ottetto: " + str(palidromo("ottetto")))
print("andrea: " + str(palidromo("andrea")))
print("otto: " + str(palidromo("otto")))