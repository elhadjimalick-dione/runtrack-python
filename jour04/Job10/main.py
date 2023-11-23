def produit_elements_dans_intervalle(liste):
    produit = 1
    for element in liste:
        if 25 <= element <= 90:
            produit *= element
    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = produit_elements_dans_intervalle(L)
print("Produit des éléments dans l'intervalle [25, 90]:", resultat)