def unAnagramma(parola1, parola2):
    return sorted(parola1) == sorted(parola2)


print(unAnagramma('Andrea', 'Aadenr'))
print(unAnagramma('Gino', 'Flavio'))
print(unAnagramma([3, 6, 8], [6, 3, 8]))