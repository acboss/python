A(m,n)

if m =  0:
    n = n+1

if m > 0 and n = 0:
    m = m-1
    n = 1

if m > 0 and n > 0:
    m = m-1
    n = A(m, n-1)

n + 1                       se m = 0
A(m - 1, 1)                 se m > 0 e n = 0
A(m - 1, A(m, n - 1))       se m > 0 e n > 0.