def cripta(testo,numeroCheCifra):
    str(testo)
    lunghezza = (len(testo))-1
    n = 0
    l = 0
    cifrata = 0
    while lunghezza > -1:
        
        a = testo[lunghezza]
        numeroLettera = ord(a)       # ord trasforma la lettera in un numero
        cifrata = numeroLettera + (numeroCheCifra)
        if testo.isupper()==False:
            if cifrata >= 123: 
                cifratajj = cifrata//122
                togli = cifrata -(cifratajj*122)
                cifrata = togli
        elif testo.isupper()==True:
            if cifrata >= 91 and cifrata :
                cifratajj = cifrata//90
                togli = cifrata -(cifratajj*90)
                cifrata = togli
    
        if cifrata == 97:
            print ('a')
        if cifrata == 98:
            print ('b')
        if cifrata == 99:
            print ('c')
        if cifrata == 100:
            print ('d')
        if cifrata == 101:
            print ('e')
        if cifrata == 102:
            print ('f')
        if cifrata == 103:
            print ('g')
        if cifrata == 104:
            print ('h')
        if cifrata == 105:
            print ('i')
        if cifrata == 106:
            print ('j')
        if cifrata == 107:
            print ('k')
        if cifrata == 108:
            print ('l')
        if cifrata == 109:
            print ('m')
        if cifrata == 110:
            print ('n')
        if cifrata == 111:
            print ('o')
        if cifrata == 112:
            print ('p')
        if cifrata == 113:
            print ('q')
        if cifrata == 114:
            print ('r')
        if cifrata == 115:
            print ('s')
        if cifrata == 116:
            print ('t')
        if cifrata == 117:
            print ('u')
        if cifrata == 118:
            print ('v')
        if cifrata == 119:
            print ('w')
        if cifrata == 120:
            print ('x')
        if cifrata == 121:
            print ('y')
        if cifrata == 122:
            print ('z')
            
            
        if cifrata == 65:
            print ('A')
        if cifrata == 66:
            print ('B')
        if cifrata == 67:
            print ('C')
        if cifrata == 68:
            print ('D')
        if cifrata == 69:
            print ('E')
        if cifrata == 70:
            print ('F')
        if cifrata == 71:
            print ('G')
        if cifrata == 72:
            print ('H')
        if cifrata == 73:
            print ('I')
        if cifrata == 74:
            print ('J')
        if cifrata == 75:
            print ('K')
        if cifrata == 76:
            print ('L')
        if cifrata == 77:
            print ('M')
        if cifrata == 78:
            print ('N')
        if cifrata == 79:
            print ('O')
        if cifrata == 80:
            print ('P')
        if cifrata == 81:
            print ('Q')
        if cifrata == 82:
            print ('R')
        if cifrata == 83:
            print ('S')
        if cifrata == 84:
            print ('T')
        if cifrata == 85:
            print ('U')
        if cifrata == 86:
            print ('V')
        if cifrata == 87:
            print ('W')
        if cifrata == 88:
            print ('X')
        if cifrata == 89:
            print ('Y')
        if cifrata == 90:
            print ('Z')
        lunghezza = lunghezza-1
        if lunghezza == -1:
            return
        








print(cripta('andrea',3))
        
