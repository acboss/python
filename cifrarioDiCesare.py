def cripta(testo,numeroCheCifra):
    str(testo)
    lunghezza = (len(testo))-1
    n = 0
    l = 0
    if 0==0 in range (lunghezza):
        a = testo[lunghezza]
        numeroLettera = ord(a)       # ord trasforma la lettera in un numero
        cifrata = numeroLettera + (numeroCheCifra)
        if cifrata >= 91:
            cifratajj = cifrata//90
            togli = cifrata -(cifratajj*90)
            cifrata = togli
            return cifrata
        elif cifrata >= 27: 
            cifratajj = cifrata//26
            togli = cifrata -(cifratajj*26)
            cifrata = togli
            return cifrata
       
        if cifrata == 1:
            print ('a')
        if cifrata == 2:
            print ('b')
        if cifrata == 3:
            print ('c')
        if cifrata == 4:
            print ('d')
        if cifrata == 5:
            print ('e')
        if cifrata == 6:
            print ('f')
        if cifrata == 7:
            print ('g')
        if cifrata == 8:
            print ('h')
        if cifrata == 9:
            print ('i')
        if cifrata == 10:
            print ('j')
        if cifrata == 11:
            print ('k')
        if cifrata == 12:
            print ('l')
        if cifrata == 13:
            print ('m')
        if cifrata == 14:
            print ('n')
        if cifrata == 15:
            print ('o')
        if cifrata == 16:
            print ('p')
        if cifrata == 17:
            print ('q')
        if cifrata == 18:
            print ('r')
        if cifrata == 19:
            print ('s')
        if cifrata == 20:
            print ('t')
        if cifrata == 21:
            print ('u')
        if cifrata == 22:
            print ('v')
        if cifrata == 23:
            print ('w')
        if cifrata == 24:
            print ('x')
        if cifrata == 25:
            print ('y')
        if cifrata == 26:
            print ('z')
            
            
        if cifrata == 65:
            print ('A')
        if cifrata == 66:
            print ('b')
        if cifrata == 67:
            print ('c')
        if cifrata == 68:
            print ('d')
        if cifrata == 69:
            print ('e')
        if cifrata == 70:
            print ('f')
        if cifrata == 71:
            print ('g')
        if cifrata == 72:
            print ('h')
        if cifrata == 73:
            print ('i')
        if cifrata == 74:
            print ('j')
        if cifrata == 75:
            print ('k')
        if cifrata == 76:
            print ('l')
        if cifrata == 77:
            print ('m')
        if cifrata == 78:
            print ('n')
        if cifrata == 79:
            print ('o')
        if cifrata == 80:
            print ('p')
        if cifrata == 81:
            print ('q')
        if cifrata == 82:
            print ('r')
        if cifrata == 83:
            print ('s')
        if cifrata == 84:
            print ('t')
        if cifrata == 85:
            print ('u')
        if cifrata == 86:
            print ('v')
        if cifrata == 87:
            print ('w')
        if cifrata == 88:
            print ('x')
        if cifrata == 89:
            print ('y')
        if cifrata == 90:
            print ('z')
        
        








cripta('andrea',3)
        
