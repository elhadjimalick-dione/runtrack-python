def trouver_max_min_valeur(liste):
    valeur = sum(liste) / len(liste)
    maximum = max(liste)
    minimum = min(liste)

    print("la valeur max est:", maximum)
    print("la valeur min est:", minimum)

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

trouver_max_min_valeur(L)