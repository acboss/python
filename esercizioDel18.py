def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    totale = x + y + z
    quadrato = b(totale)**2
    return quadrato


x = 1
y = x + 1
print(c(x, y+3, x+y))