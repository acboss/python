def stampa2volte(t):
    print(t)
    print(t)

def fai2volte(f, x):
    f(x)
    f(x)
    

def stampa_spam(y):
    print(y)


c = "spam"
fai2volte(stampa_spam, c)

