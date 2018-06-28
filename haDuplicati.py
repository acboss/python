def ha_duplicati():
    t = list(s)
    t.sort()

    # check for adjacent elements that are equal
    for i in range(len(t)-1):
        if parola[i] == parola[i+1]:
            return True
    return False


print(ha_duplicati('cba'))
print(ha_duplicati('abba'))