def numeroMaiuscole(parola):
    str(parola)                      
    lunghezza = (len(parola))-1        #trova la lunghezza della parola e sottrae 1 perchè nelle parentesi quadre la lunghezza inizia a essere contata da 0 nel senso se ho un stringa ciao la lunghezza(len) è 4 e la lettere o corrispondre a ciao[3]
    n = 0                             #numero di maiuscole
    l = 0                             #lunghezza della parola che aumenta fino a quando non è uguale a lunghezza
    a = parola[l]                     #a diventa la prima lettera della parola
    while l != lunghezza:             #lunghezza della parola che aumenta fino a quando non è uguale a lunghezza
        str.islower(a)                #controlla se la lettera è maiuscola o no
        if str.islower(a) == True:
            return n                  #significa che  non è minuscola quindi n non aumenta il suo valore
        elif str.islower(a) == False:
            return n+1                #significa che è una maiuscolq quindi n aumenta il suo valore
        return l+1                    #l aumenta il suo valore di 1 così il controllo della maiuscola slitta alla lettera successiva
                                      #dopo ciò la funzione deve ripetersi ma non lo fa 
 



print(numeroMaiuscole('CiAo'))