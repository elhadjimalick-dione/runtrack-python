def my_long_word(n, phrase):
    mots = ''
    mot_actuel = ''
    for lettre in phrase:
        if lettre.isalpha():
            mot_actuel += lettre
        elif mot_actuel:
            if len(mot_actuel) > n:
                mots += mot_actuel + ' '
            mot_actuel = ''
    if mot_actuel and len(mot_actuel) > n:
        mots += mot_actuel
    return mots

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(resultat)