def my_sort(lst):
    coups = 0  # Initialiser le compteur de coups
    swapped = True  # Initialiser le drapeau d'échange

    while swapped:
        swapped = False  # Réinitialiser le drapeau d'échange à chaque itération
        for i in range(len(lst) - 1):
            # Comparer les éléments adjacents et les échanger si nécessaire
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True  # Mettre à jour le drapeau d'échange
                coups += 1  # Incrémenter le compteur de coups

    print("Nombre total de coups nécessaires :", coups)
    return lst

# Exemple d'utilisation
ma_liste = [4, 2, 7, 1, 9, 5]
resultat = my_sort(ma_liste)
print("Liste triée :", resultat)