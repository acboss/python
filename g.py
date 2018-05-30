def fai2volte(f,x):
    f(x)
    f(x)

def stampa2volte(t):
    print(t)
    print(t)

def fai_quattro (f,x):
    fai2volte(f, x)
    fai2volte(f, x)

fai2volte(stampa2volte, "spam")
print(" ")
fai_quattro(fai2volte, "spam")