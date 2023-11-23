def compter_multiples_de_3(liste):
    compter_multiples_de_3 = [i for i in liste if i % 3 == 0]
    return len(compter_multiples_de_3)

L = [8, 24, 48, 2, 16]
print(compter_multiples_de_3(L))