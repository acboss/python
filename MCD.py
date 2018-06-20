def MCD(a,b):
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b



print (MCD (48,36))

