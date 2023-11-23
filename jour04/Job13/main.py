def supprimer_doublons(liste):

    liste_unique = []

    i = 0
    while i < len(liste):
        element = liste[i]

        j = 0
        element_present = False
        while j < len(liste_unique):
            if liste_unique[j] == element:
                element_present = True
                break
            j += 1

        if not element_present:
            liste_unique.append(element)

        i += 1

    return liste_unique

ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = supprimer_doublons(ma_liste)

print("Liste sans doublons :", liste_sans_doublons)