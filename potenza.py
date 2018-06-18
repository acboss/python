def potenza(a,b):
    if a%b == 0 and (a/b)%b == 0:
        return True
    else:
        return False

# dovevi mettere il risultato del def "potenza" in una variabile, ho aggiunto "x ="
x = potenza (144, 12)

# e poi stamparla

print(x)

# in alternativa, come hai fatto nei palindromi, potevi direttamente stampare "potenza":  print(potenza (144, 12)) 


# l'unico limite del programma è che lui controlla se il primo numero è la potenza del secondo, ma non viceversa. 
# per farlo calcolare indipendentemente dall'ordine con cui immetti la base e la potenza devi, se il risultato è falso (quindi dopo l'else) 
# concatenare un altro if copiando le formule del primo ma invertendo a e b, in questo modo il programma controlla se b è una potenza di a.
# solo se entrambi gli if falliscono restituisci false, altrimenti restituisci true.
# vedi se conviene usare elseif invece di un secondo if dentro all'else, dato che python lo ha