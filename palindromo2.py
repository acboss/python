
def palindromo2(parola):
    str(parola)
    parolaAlContrario = parola[::-1]
    if parola == parolaAlContrario:
        return True
    else:
        return str(False) + " " + parola[::-1]

# ho aggiunto una stringa a ciò che stampi in modo che si capisca meglio quali parole hai analizzato per vedere se sono palindrome o meno
print("ottetto: " + str(palindromo2("ottetto")))
print("andrea: " + str(palindromo2("andrea")))
print("otto: " + str(palindromo2("otto")))
