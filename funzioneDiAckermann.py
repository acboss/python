def A(m,n):
    if m = 0:
        g = n
        n = g+1
        return
    if m > 0 and n = 0:
        s = m
        m = s-1
        n = 1
        return
    if m > 0 and n > 0:
        p = m
        n = d
        m = p-1
        n = A(m, d-1)
        return

print (A(3,4))
