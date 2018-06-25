def numeroMaiuscole(parola):
    str(parola)                      
    lunghezza = (len(parola))-1
    n = 0
    l = -1
    a = parola[l]
    while l != lunghezza:
        l+1
        str.islower(a)
        if str.islower(a) == True:
            return n+1 
        elif str.islower(a) == False:
            return n




print(numeroMaiuscole('CiAo'))