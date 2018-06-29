fin = open('words.txt')
def cerca(parolaCercata):
    if parolaCercata in fin:
        return True
    else:
        return False





parola = 'aa'
parolaCercata = parola + '\n'
print(cerca(parola))


