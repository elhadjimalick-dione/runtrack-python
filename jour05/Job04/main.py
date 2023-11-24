def afficher_tapis_diagonale(n):
    for i in range(n + 1):
        ligne = "|"
        for j in range(n + 1):
            if j == n - i:
                ligne += " "
            else:
                ligne += "#"
        ligne += "|"
        print(ligne)


afficher_tapis_diagonale(10)