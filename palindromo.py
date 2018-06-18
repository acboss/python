def prima(parola):
    return parola[0]
def ultima(parola):
    return parola[-1]
def mezzo(parola):
    return parola[1:-1]

def palidromo(parola):
    if len(parola) <= 1:
        return True
    if prima(parola) != ultima(parola)
        return False
    return palidromo(mezzo(parola))


print(palidromo("ottetto"))
print(palidromo("andrea"))
print(palidromo("otto"))