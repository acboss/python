import math

def mia_radq(a):
    if a > 1:
        x = a
    if a <= 1:
        x = 1
    while True:
        y = float((x + a/x) / 2)
        if y == x:
            break 
        x = y
        
    return x


def test(a):
    print ("a                 mia_radq(a)                      math.sqrt(a)                     diff \n----   ----------    ------------   ---- ")
    q = str(float(a))
    w = str(mia_radq(a))
    e = math.sqrt(a)
    r = mia_radq(a) 
    g = str(e)
    p = r - e
    t = str(p) 
    print (q + "              " + w + "                               " + g + "                               " + t)

test(41)