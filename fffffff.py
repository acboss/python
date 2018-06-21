def una_minuscola1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def una_minuscola2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def una_minuscola3(s):
    for c in s:
        flag = c.islower()
        return flag

def una_minuscola4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def una_minuscola5(s):
    for c in s:
        if not c.islower():
            return False
    return True


#print(str.islower('ciao'))
#print(str.islower('cIao'))
#print(str(len('ciao')))

def numeroMaiuscole(parola):
    str(parola)
    lunghezza = (len(parola))-1
    n = 0
    if len >= 0:
        a = parola[lunghezza-1]
        str.islower(a)
        if str.islower(a) == True:
            return n+1
        elif str.islower(a) == False:
            return n

print(numeroMaiuscole('CiAo'))
