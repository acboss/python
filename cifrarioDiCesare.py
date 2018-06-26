def cripta(testo,numeroCheCifra):
    str(testo)
    lunghezza = (len(testo))-1
    n = 0
    l = 0
    cifrata = 0
    testoCriptato = ''
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
        else:
            if (122>= cifrata =<96) or (91>= cifrata <=64):
                testoCriptato += a
        if cifrata == 97:
            testoCriptato +=  'a'
        if cifrata == 98:
            testoCriptato +=  'b'
        if cifrata == 99:
            testoCriptato +=  'c'                       
        if cifrata == 100:
           testoCriptato +=  'd'
        if cifrata == 101:
            testoCriptato +=  'e'
        if cifrata == 102:
            testoCriptato +=  'f'
        if cifrata == 103:
            testoCriptato +=  'g'
        if cifrata == 104:
            testoCriptato +=  'h'
        if cifrata == 105:
            testoCriptato +=  'i'
        if cifrata == 106:
            testoCriptato +=  'j'
        if cifrata == 107:
            testoCriptato +=  'k'
        if cifrata == 108:
            testoCriptato +=  'l'
        if cifrata == 109:
            testoCriptato +=  'm'
        if cifrata == 110:
            testoCriptato +=  'n'
        if cifrata == 111:
            testoCriptato +=  'o'
        if cifrata == 112:
            testoCriptato +=  'p'
        if cifrata == 113:
            testoCriptato +=  'q'
        if cifrata == 114:
            testoCriptato +=  'r'
        if cifrata == 115:
            testoCriptato +=  's'
        if cifrata == 116:
            testoCriptato +=  't'
        if cifrata == 117:
            testoCriptato +=  'u'
        if cifrata == 118:
            testoCriptato +=  'v'
        if cifrata == 119:
            testoCriptato +=  'w'
        if cifrata == 120:
            testoCriptato +=  'x'
        if cifrata == 121:
            testoCriptato +=  'y'
        if cifrata == 122:
            testoCriptato +=  'z'
        if cifrata == 65:
            testoCriptato +=  'A'
        if cifrata == 66:
            testoCriptato +=  'B'
        if cifrata == 67:
            testoCriptato +=  'C'
        if cifrata == 68:
            testoCriptato +=  'D'
        if cifrata == 69:
            testoCriptato +=  'E'
        if cifrata == 70:
            testoCriptato +=  'F'
        if cifrata == 71:
            testoCriptato +=  'G'
        if cifrata == 72:
            testoCriptato +=  'H'
        if cifrata == 73:
            testoCriptato +=  'I'
        if cifrata == 74:
            testoCriptato +=  'J'
        if cifrata == 75:
            testoCriptato +=  'K'
        if cifrata == 76:
            testoCriptato +=  'L'
        if cifrata == 77:
            testoCriptato +=  'M'
        if cifrata == 78:
            testoCriptato +=  'N'
        if cifrata == 79:
            testoCriptato +=  'O'
        if cifrata == 80:
            testoCriptato +=  'P'
        if cifrata == 81:
            testoCriptato +=  'Q'
        if cifrata == 82:
            testoCriptato +=  'R'
        if cifrata == 83:
            testoCriptato +=  'S'
        if cifrata == 84:
            testoCriptato +=  'T'
        if cifrata == 85:
            testoCriptato +=  'U'
        if cifrata == 86:
            testoCriptato +=  'V'
        if cifrata == 87:
            testoCriptato +=  'W'
        if cifrata == 88:
            testoCriptato +=  'X'
        if cifrata == 89:
            testoCriptato +=  'Y'
        if cifrata == 90:
            testoCriptato +=  'Z'
        
        lunghezza = lunghezza-1
        if lunghezza == -1:
            print(testoCriptato[::-1])
        



cripta('Andrea',3)
        
