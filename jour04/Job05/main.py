L = [1, 2, 3, 4, 5]

print("Deuxième valeur de la liste:", L[1])

def remplacer_valeur(liste):
    somme_voisins = liste[2] + liste[4]
    liste[3] = somme_voisins

remplacer_valeur(L)

print("Liste après la modification:", L)
print("Dernière valeur de la liste:", L[-1])