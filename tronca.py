def tronca(numeri):
    del numeri[0]
    del numeri[-1]

numeri = [1,2,3,4]
tronca(numeri)
print(numeri)