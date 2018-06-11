def contoallarovescia(n):
    if n <= 0:
        print('Via!')
    else:
        print(n)
        contoallarovescia(n-1)


def stampa_n(s, n):
    if n <= 0:
        return
    print(s)
    stampa_n(s, n-1)

def fai_n(j,n):
    if n <= 0:
        return
    elif n>0:
        j
        fai_n(j,n-1)
        
#Come esercizio, disegnate il diagramma di stack della funzione stampa_n chiamata con
#s=Ciao e n=2. Poi, scrivete una funzione di nome fai_n che accetti come argomenti un
#oggetto funzione e un numero n, e che chiami per n volte la funzione data
N = 2
S = 'ciao'
stampa_n(S,N)
fai_n(stampa_n(S,N),N)
